from Utils import getIdFromSession
from flask import Response, request, session
from flask_restful import Resource
from database.models import Product_images, Wish_list, seshion, Product, Reviews, User, Books, Accessories
import json

class GetProducts(Resource):
    def get(self):
        res = seshion.query(Product.product_id).order_by(
            Product.added_at.desc())
        p_ids = []
        for i in res:
            p_ids.append(i[0])
        prods = []
        for i in p_ids:
            dic = {}
            p = seshion.query(Product.product_id, Product.brand_name, Product.category,
                              Product.description, Product.title, Product.price, Product.discount).filter(Product.product_id == i).all()
            img = seshion.query(Product_images.image_path).filter(
                Product_images.product_id == i).all()
            dic['prod_id'] = p[0][0]
            dic['brand'] = p[0][1]
            dic['category'] = p[0][2]
            dic['description'] = p[0][3]
            dic['title'] = p[0][4]
            dic['price'] = p[0][5]
            dic['discount'] = p[0][6]
            dic['img_path'] = img[0][0]
            #
            dic['isFavourite'] = False
            prods.append(dic)
        return Response(json.dumps(prods), status=200)


class AddInWishList(Resource):
    def post(self,p_id):
        id = getIdFromSession()
        print(id)
        if(id != None):
            try:
                w=Wish_list(buyer_id=id,product_id=p_id)
                seshion.add(w)
                seshion.commit()
                return Response('true',status=200)
            except Exception as e:
                return Response('false',status=200)
        else:
            return Response('false',status=200)


class GetWishListProducts(Resource):
    def get(self):
        id=session.get('id')
        if(id==None):
            return Response([],status=200)
        else:
            res = seshion.query(Wish_list.product_id).filter(Wish_list.buyer_id==id).all()
            p_ids = []
            for i in res:
                p_ids.append(i[0])
            prods = []
            for i in p_ids:
                dic = {}
                p = seshion.query(Product.product_id, Product.brand_name, Product.category,
                                Product.description, Product.title, Product.price, Product.discount).filter(Product.product_id == i).all()
                img = seshion.query(Product_images.image_path).filter(
                    Product_images.product_id == i).all()
                dic['prod_id'] = p[0][0]
                dic['brand'] = p[0][1]
                dic['category'] = p[0][2]
                dic['description'] = p[0][3]
                dic['title'] = p[0][4]
                dic['price'] = p[0][5]
                dic['discount'] = p[0][6]
                dic['img_path'] = img[0][0]
                dic['isFavourite'] = True
                prods.append(dic)
            return Response(json.dumps(prods), status=200)

class AddToCart(Resource):
    def post(self, p_id):
        id=session.get('id')
        print(id)
        print(p_id)
        if(id==None):
            return Response(False,status=200)
        else:
            session['cart']= session.get('cart') + ' ' + p_id
            print(session.get('cart'))
            return Response(True,status=200)

class GetCartProducts(Resource):
    def get(self):
        id=session.get('id')
        if(id==None):
            return Response([],status=200)
        else:
            p_ids=session.get('cart')
            p_ids=p_ids.split(' ')
            isFirst=True
            prods=[]
            for i in p_ids:
                if(not isFirst):
                    dic = {}
                    p = seshion.query(Product.product_id, Product.brand_name, Product.category,
                                    Product.description, Product.title, Product.price, Product.discount).filter(Product.product_id == i).all()
                    img = seshion.query(Product_images.image_path).filter(
                        Product_images.product_id == i).all()
                    dic['prod_id'] = p[0][0]
                    dic['brand'] = p[0][1]
                    dic['category'] = p[0][2]
                    dic['description'] = p[0][3]
                    dic['title'] = p[0][4]
                    dic['price'] = p[0][5]
                    dic['discount'] = p[0][6]
                    dic['img_path'] = img[0][0]
                    dic['isFavourite'] = True
                    prods.append(dic)
                else:
                    isFirst=False
            return Response(json.dumps(prods), status=200)

class getProductsSpecification(Resource):
    def get(self):
        p_id=request.args.get('p_id')
        category=request.args.get('category')
        if(category=='books'):
            return Response(json.dumps(getBooks(p_id)),status=200)
        elif(category=='laptop'):
            pass
        elif(category=='mobile'):
            pass
        else:
            return Response(json.dumps(getAccessories(p_id)),status=200)


def getBooks(p_id):
        p = seshion.query(Product.product_id, Product.brand_name, Product.category,
                                Product.description, Product.title, Product.price, Product.discount, Product.rating_counter).filter(Product.product_id == p_id).all()
        b=seshion.query(Books.author,Books.isbn,Books.edition).filter(Books.product_id==p_id)
        img = seshion.query(Product_images.image_path).filter(
                Product_images.product_id == p_id).all()
        dic={}
        dic['prod_id'] = p[0][0]
        dic['brand'] = p[0][1]
        dic['category'] = p[0][2]
        dic['description'] = p[0][3]
        dic['title'] = p[0][4]
        dic['price'] = p[0][5]
        dic['discount'] = p[0][6]
        dic['rating']=p[0][7]
        #category wise
        dic['author']=b[0][0]
        dic['isbn']=b[0][1]
        dic['edition']=b[0][2]
         #images
        images=len(img)
        dic['img1_path'] = img[0][0]
        dic['img2_path'] = ''
        dic['img3_path'] = ''
        dic['img4_path'] = ''
        if(images>1):
            dic['img2_path'] = img[1][0]
        if(images>2):
            dic['img3_path'] = img[2][0]
        if(images>3):
            dic['img4_path'] = img[3][0]
        return dic

def getMobile(p_id):
    pass
def getLaptop(p_id):
    pass
def getAccessories(p_id):
    p = seshion.query(Product.product_id, Product.brand_name, Product.category,
                                Product.description, Product.title, Product.price, Product.discount, Product.rating_counter).filter(Product.product_id == p_id).all()
    acc=seshion.query(Accessories.color).filter(Accessories.product_id==p_id)
    img = seshion.query(Product_images.image_path).filter(
                Product_images.product_id == p_id).all()
    print(len(img))
    colors=[]
    for i in acc:
        colors.append(i[0])
    dic={}
    dic['prod_id'] = p[0][0]
    dic['brand'] = p[0][1]
    dic['category'] = p[0][2]
    dic['description'] = p[0][3]
    dic['title'] = p[0][4]
    dic['price'] = p[0][5]
    dic['discount'] = p[0][6]
    dic['rating']=p[0][7]
    #colors
    dic['colors']=colors
    #images
    images=len(img)
    dic['img1_path'] = img[0][0]
    dic['img2_path'] = ''
    dic['img3_path'] = ''
    dic['img4_path'] = ''
    if(images>1):
        dic['img2_path'] = img[1][0]
    if(images>2):
        dic['img3_path'] = img[2][0]
    if(images>3):
        dic['img4_path'] = img[3][0]
    return dic

class getReviewsByProductId(Resource):
    def get(self,p_id):
        res=seshion.query(Reviews.buyer_id,Reviews.reviews).filter(Reviews.product_id==p_id).all()
        lst=[]
        for i in res:
            dic={}
            username=seshion.query(User.user_name).filter(User.user_id==i[0]).all()
            dic['username']=username[0][0]
            dic['review']=i[1]
            lst.append(dic)
        return Response(json.dumps(lst),status=200)