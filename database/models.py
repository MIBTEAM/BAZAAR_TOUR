import json
from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, Integer, PrimaryKeyConstraint, String, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    or_, create_engine, DateTime
)

engine = create_engine("sqlite:///BazaarTour.db",
                       connect_args={'check_same_thread': False}, echo=True)
Session = sessionmaker(bind=engine)
seshion = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    user_id = Column(String(50), primary_key=True)
    email = Column(String(70), unique=True, nullable=False)
    user_name = Column(String(50), unique=True, nullable=False)
    password = Column(String(70), nullable=False)
    cnic = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    contact_no = Column(String(15), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True))
    buyer = relationship("Buyer", back_populates="buyer_table",
                         uselist=False, cascade='save-update, merge, delete')
    seller = relationship("Seller", back_populates="seller_table",
                          uselist=False, cascade='save-update, merge, delete')
    administration = relationship(
        "Administration", back_populates="admin_table", cascade='save-update, merge, delete')

    def __repr__(self):
        return f"user_name : {self.user_name}"

    # def insertUser(userid, email, username, password, cnic, firstname, lastname, cnicNo, isActive, contactNo):
    #     usr = User(user_id=userid, email=email, user_name=username, password=password,
    #                cnic=cnicNo, first_name=firstname, last_name=lastname, ia_active=isActive, contact_no=contactNo)
    #     session.add(usr)
    #     session.commit()

# Adminstration have on-to-one relationship with user and seller


class Administration(Base):
    __tablename__ = "administration"
    administration_id = Column(String(50), ForeignKey("user.user_id"))
    seller_id = Column(String(50), ForeignKey("seller.seller_id"))
    comments = Column(String(3000), nullable=False)
    # seller_info=relationship("Seller", back_populates="seller_status")
    admin_table = relationship("User", back_populates="administration")
    __table_args__ = (
        PrimaryKeyConstraint(administration_id, seller_id),
    )

    def __repr__(self):
        return f"Seller ID : {self.seller_id}"


# buyer have on-to-one relationship with user and one-to-many with wish_list and reviews
class Buyer(Base):
    __tablename__ = "buyer"
    buyer_id = Column(String(50), ForeignKey("user.user_id"), primary_key=True)
    province = Column(String(30), nullable=False)
    city = Column(String(40), nullable=False)
    area = Column(String(5000), nullable=False)
    land_mark = Column(String(1000), nullable=True)
    buyer_table = relationship("User", back_populates="buyer")
    buyer_wish_rel = relationship("Wish_list", back_populates="wish_buyer_rel",
                                  uselist=False, cascade='save-update, merge, delete')
    buyer_review = relationship(
        "Reviews", back_populates="buyer_review_rel", cascade='save-update, merge, delete')

    def __repr__(self):
        return f"Buyer ID : {self.buyer_id}"


# seller have on-to-one relationship with user and adminstration
class Seller(Base):
    __tablename__ = "seller"
    seller_id = Column(String(50), ForeignKey(
        "user.user_id"), primary_key=True)
    # admin_id=Column(String(50),ForeignKey("administration.administration_id"))
    profile_pic = Column(String(100), nullable=False)
    cnic_front = Column(String(50), nullable=False)
    cnic_back = Column(String(50), nullable=False)
    store_name = Column(String(40), nullable=False)
    account_balance = Column(Float, default=0.0, nullable=False)
    brand_logo = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    pick_province = Column(String(30), nullable=False)
    pick_city = Column(String(40), nullable=False)
    pick_area = Column(String(5000), nullable=False)
    pick_land_mark = Column(String(1000), nullable=True)
    return_province = Column(String(30), nullable=False)
    return_city = Column(String(40), nullable=False)
    return_area = Column(String(5000), nullable=False)
    return_land_mark = Column(String(1000), nullable=True)
    revenue = Column(Float, default=0.0, nullable=False)
    saled_products = Column(Integer, default=0, nullable=False)
    rating = Column(Float, default=0.0, nullable=False)
    bank_name = Column(String(100), nullable=False)
    bank_account_no = Column(String(100), nullable=False)
    is_approved = Column(Boolean, nullable=False, default=False)
    seller_table = relationship("User", back_populates="seller")
    product_list = relationship("Product", back_populates="seller_product_rel")
    orders_list = relationship(
        "Seller_orders", back_populates="seller_orders_list")
    # seller_status=relationship("Adminstration", back_populates="seller_info")

    def __repr__(self):
        return f"Seller ID : {self.seller_id}"


# relationship one-to-many with buyer and many-to-one with product
class Wish_list(Base):  # problem: in processing if put seller_id also to get data easily
    __tablename__ = "wish_list"
    buyer_id = Column(String(50), ForeignKey("buyer.buyer_id"))
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    wish_buyer_rel = relationship("Buyer", back_populates="buyer_wish_rel")
    wish_product_rel = relationship("Product", back_populates="product_rel")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, buyer_id),
    )

    def __repr__(self):
        return f"Buyer ID : {self.buyer_id}"

class Orders(Base):  # problem :  make seller and order one-to many relation for easy dashborad processing
    __tablename__ = "order"
    order_id = Column(BigInteger().with_variant(
        Integer, "sqlite"), primary_key=True)
    buyer_id = Column(String(50), ForeignKey("buyer.buyer_id"))
    placed_at = Column(DateTime(timezone=True), server_default=func.now())
    payment_method = Column(String(20), nullable=False)  # determined
    delivery_status = Column(String(30), nullable=False)  # determined
    order_rel = relationship("Products_in_orders",
                             back_populates="product_list")

    def __repr__(self):
        return f"Order ID : {self.order_id}"


class Seller_orders(Base):
    __tablename__ = "seller_orders"
    seller_id = Column(String(50), ForeignKey("seller.seller_id"))
    order_id = Column(BigInteger, ForeignKey("order.order_id"))
    is_viewed = Column(Boolean, default=False, nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(order_id, seller_id),
    )
    seller_orders_list = relationship("Seller", back_populates="orders_list")

    def __repr__(self):
        return f"Order ID : {self.order_id}"

# relation with orders many-to-one


class Products_in_orders(Base):
    __tablename__ = "products_in_order"
    order_id = Column(BigInteger, ForeignKey("order.order_id"))
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    quantity = Column(Integer, default=0, nullable=False)
    product_list = relationship("Orders", back_populates="order_rel")
    __table_args__ = (
        PrimaryKeyConstraint(order_id, product_id),
    )

    def __repr__(self):
        return f"Order ID : {self.order_id}"


# relationship with many-to-one seller , one-to-many product_images, books ,accessories,computing_devices,reviews


class Product(Base):
    __tablename__ = "products"
    product_id = Column(BigInteger().with_variant(
        Integer, "sqlite"), primary_key=True)
    seller_id = Column(String(50), ForeignKey("seller.seller_id"))
    title = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    brand_name = Column(String(100), nullable=False)
    description = Column(String(5000), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Integer, default=0, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    added_at = Column(DateTime(timezone=True), server_default=func.now())
    rating_counter = Column(Float, default=0, nullable=False)
    img_path = relationship("Product_images", back_populates="images_list")
    product_rel = relationship(
        "Wish_list", back_populates="wish_product_rel", cascade='save-update, merge, delete')
    product_review = relationship(
        "Reviews", back_populates="product_review_rel", cascade='save-update, merge, delete')
    book_rel = relationship("Books", back_populates="book_product_rel",
                            uselist=False, cascade='save-update, merge, delete')
    computing_rel = relationship("Computing_devices", back_populates="computing_product_rel",
                                 uselist=False, cascade='save-update, merge, delete')
    accessories_rel = relationship(
        "Accessories", back_populates="accessories_product_rel", cascade='save-update, merge, delete')
    seller_product_rel = relationship("Seller", back_populates="product_list")

    def __repr__(self):
        return f"Product ID : {self.product_id}"

# relation many-to-one with product


class Product_images(Base):
    __tablename__ = "product_images"
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    image_path = Column(String(150), nullable=False)
    images_list = relationship("Product", back_populates="img_path")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, image_path),
    )

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# relationship many-to-one with product
class Reviews(Base):
    __tablename__ = "reviews"
    review_id = Column(BigInteger().with_variant(
        Integer, "sqlite"), primary_key=True)
    buyer_id = Column(String(50), ForeignKey("buyer.buyer_id"))
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    reviews = Column(String(5000), nullable=True)
    buyer_review_rel = relationship("Buyer", back_populates="buyer_review")
    product_review_rel = relationship(
        "Product", back_populates="product_review")

    def __repr__(self):
        return f"Reviews ID : {self.review_id}"


# relationship many-to-one with product
class Books(Base):
    __tablename__ = "books"
    product_id = Column(BigInteger, ForeignKey(
        "products.product_id"), primary_key=True)
    isbn = Column(String(20), nullable=False)
    author = Column(String(100), nullable=False)
    edition = Column(String(20), nullable=True)
    book_product_rel = relationship("Product", back_populates="book_rel")

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# relationship many-to-one with product
class Computing_devices(Base):
    __tablename__ = "computing_devices"
    product_id = Column(BigInteger, ForeignKey(
        "products.product_id"), primary_key=True)
    ram = Column(String(20), nullable=False)
    hard = Column(String(20), nullable=False)
    processor = Column(String(20), nullable=False)
    dimension = Column(String(20), nullable=False)
    computing_product_rel = relationship(
        "Product", back_populates="computing_rel")
    compt_color_list_rel = relationship(
        "Computing_devices_color", back_populates="compt_color_rel", cascade='save-update, merge, delete')
    laptop_rel = relationship("Laptop", back_populates="laptop_product_rel",
                              uselist=False, cascade='save-update, merge, delete')
    mobile_rel = relationship("Mobile", back_populates="mobile_product_rel",
                              uselist=False, cascade='save-update, merge, delete')

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# relationship many-to-one with computing_devices
class Computing_devices_color(Base):
    __tablename__ = "computing_devices_color"
    product_id = Column(BigInteger, ForeignKey("computing_devices.product_id"))
    color = Column(String(20), nullable=False)
    compt_color_rel = relationship(
        "Computing_devices", back_populates="compt_color_list_rel")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, color),
    )

    def __repr__(self):
        return f"Product ID : {self.color}"


# relationship one-to-one with computing_devices
class Laptop(Base):
    __tablename__ = "laptop"
    product_id = Column(BigInteger, ForeignKey("computing_devices.product_id"))
    generation = Column(String(20), nullable=False)
    laptop_product_rel = relationship(
        "Computing_devices", back_populates="laptop_rel")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, generation),
    )

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# relationship one-to-one with computing_devices
class Mobile(Base):
    __tablename__ = "mobile"
    product_id = Column(BigInteger, ForeignKey("computing_devices.product_id"))
    camera_pixels = Column(String(20), nullable=False)
    mobile_product_rel = relationship(
        "Computing_devices", back_populates="mobile_rel")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, camera_pixels),
    )

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# relationship many-to-one with product
class Accessories(Base):
    __tablename__ = "accessories"
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    color = Column(String(20), nullable=False)
    accessories_product_rel = relationship(
        "Product", back_populates="accessories_rel")
    __table_args__ = (
        PrimaryKeyConstraint(product_id, color),
    )

    def __repr__(self):
        return f"Product ID : {self.product_id}"


# Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)

# temp = Product(seller_id='BTS412023191549945', title='hand free', category='accessories', brand_name='audionic', description='hand free everything ok',
#            price=765, discount=10, stock=50)

# temp=Accessories(product_id=9,color='red')
# seshion.add(temp)
# seshion.commit()

# temp = Product_images(product_id=6, image_path='img6')

# temp = Books(product_id=7, isbn='12345678710987',
#              author='laiba tariq', edition=7)
# o = Orders(buyer_id='BTB41202319125287',
#            payment_method='online', delivery_status='placed')

# m = Mobile(product_id=6, camera_pixels='20')
# temp = Seller_orders(seller_id='BTS412023191549945', order_id=4)
# temp = Products_in_orders(order_id=5, product_id=6, quantity=6)
# seshion.add(temp)
# seshion.commit()
# orders = seshion.query(Seller_orders.order_id, Seller_orders.seller_id).filter(
#     Seller_orders.seller_id == 'BTS412023191549945').all()
# print(json.dumps(dict(orders)))

# print(seshion.query(Seller_orders.seller_orders_list).all())
# ids = seshion.query(Seller_orders.order_id, Seller_orders).filter(
#     Seller_orders.seller_id == 'BTS412023191549945').all()
# list = []
# for i in ids:
#     list.append(i[0])
# ids = list
# res = seshion.query(Products_in_orders).join(Product).filter(
#     Products_in_orders.order_id.in_(ids)).all()
# print(res)




# print(prods)
# p = seshion.query(Product.product_id, Product.brand_name, Product.category,
#                   Product.description, Product.title, Product.price, Product.discount).filter(Product.product_id == 1).all()
# print(p[0])
# print(img[0][0])
# print(res)
# print(p_ids)


# seshion.query(Product_images).filter(Product_images.product_id == 7, Product_images.image_path == '2nd imnage path').update(
#     {Product_images.image_path: "/sellerData/BTS412023191549945/product/7/img1.jpg"}, synchronize_session=False)
# seshion.commit()




# res=seshion.query(User.user_id).filter(User.email=='abdulwahhaab111@gmail.com', User.password=='Qwer1234').all()
# print(res[0][0])

# i=Product_images(product_id=10,image_path='/sellerData/BTS412023191549945/product/9/img1.jpg')
# seshion.add(i)
# seshion.commit()

# r=Reviews(buyer_id='BTB41202319125287',product_id=1,reviews='what are you doing')
# seshion.add(r)
# seshion.commit()