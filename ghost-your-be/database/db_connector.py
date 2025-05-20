from sqlalchemy import create_engine, Table, Column, Integer, String, Float, Boolean, MetaData
from sqlalchemy.exc import SQLAlchemyError
import pymongo
import urllib.parse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBConnector:
    def __init__(self, db_url):
        self.db_url = db_url
        self.is_sql = not db_url.startswith("mongodb://")
        self.connection = None
        try:
            if self.is_sql:
                self.engine = create_engine(db_url, echo=False)
                self.metadata = MetaData()
                self.connection = self.engine.connect()
                logger.info(f"Kết nối thành công với SQL database: {db_url}")
            else:
                self.mongo_client = pymongo.MongoClient(db_url)
                db_name = urllib.parse.urlparse(db_url).path.lstrip("/")
                self.mongo_db = self.mongo_client[db_name]
                logger.info(f"Kết nối thành công với MongoDB: {db_url}")
        except (SQLAlchemyError, pymongo.errors.PyMongoError) as e:
            logger.error(f"Lỗi khi kết nối tới database: {e}")
            raise

    def _map_python_type_to_sql(self, value):
        """Ánh xạ kiểu Python sang kiểu SQLAlchemy."""
        if isinstance(value, str):
            return String
        elif isinstance(value, int):
            return Integer
        elif isinstance(value, float):
            return Float
        elif isinstance(value, bool):
            return Boolean
        else:
            return String  # Mặc định là String nếu không xác định được

    def save_to_db(self, table_name, data):
        """Lưu dữ liệu vào database (SQL hoặc MongoDB)."""
        if not data:
            logger.warning("Không có dữ liệu để lưu!")
            return False

        try:
            if self.is_sql:
                # Tạo bảng động cho SQL database
                columns = [Column('id', Integer, primary_key=True)]
                for key, value in data[0].items():
                    col_type = self._map_python_type_to_sql(value)
                    columns.append(Column(key, col_type))
                
                table = Table(table_name, self.metadata, *columns)
                self.metadata.create_all(self.engine)
                
                # Lưu dữ liệu theo batch
                batch_size = 1000
                for i in range(0, len(data), batch_size):
                    self.connection.execute(table.insert(), data[i:i+batch_size])
                logger.info(f"Lưu {len(data)} bản ghi vào bảng {table_name} (SQL)")
                return True
            else:
                # Lưu vào MongoDB collection
                collection = self.mongo_db[table_name]
                collection.insert_many(data, ordered=False)
                logger.info(f"Lưu {len(data)} bản ghi vào collection {table_name} (MongoDB)")
                return True
        except (SQLAlchemyError, pymongo.errors.PyMongoError) as e:
            logger.error(f"Lỗi khi lưu vào database: {e}")
            return False

    def close(self):
        """Đóng kết nối database."""
        if self.is_sql and self.connection:
            self.connection.close()
            self.engine.dispose()
            logger.info("Đóng kết nối SQL database")
        elif not self.is_sql:
            self.mongo_client.close()
            logger.info("Đóng kết nối MongoDB")