from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

# select * from table_all
def get_all_products(db: Session):
    """
    funcao que retorna todos os elementos
    """
    return db.query(ProductModel).all()

# select * from where id = id
def get_product(db: Session, product_id: int):
    """
    funcao que recebe um id e retorna somente ele
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# insert into (create)
def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump()) # transformar minha view para ORM
    db.add(db_product) # adicionar na tabela
    db.commit() # commitar na minha tabela
    db.refresh(db_product) # fazer o refresh do banco de dados
    return db_product # retornar para o user o item criado

# delete * from table where id = id
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

# update * from where id = id
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    db.refresh(db_product)
    return db_product