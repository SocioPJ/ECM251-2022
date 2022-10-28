from src.dao.product_dao import ProductDAO

items = ProductDAO.get_instance().get_all()