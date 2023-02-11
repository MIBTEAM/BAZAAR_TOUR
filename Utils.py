from flask import session
from operatingSystem import *
from database.models import User, seshion, Seller, Buyer


def addSellerInSession(request):
    mail = request.form.get('email')
    id = request.form.get('userid')
    session['firstname'] = request.form.get('firstname')
    session['lastname'] = request.form.get('lastname')
    session['username'] = request.form.get('username')
    session['userid'] = id
    session['email'] = mail
    session['password'] = request.form.get('password')
    session['cntct'] = request.form.get('cntct')
    session['cnic'] = request.form.get('cnic')
    session['storename'] = request.form.get('storename')
    session['province'] = request.form.get('province')
    session['city'] = request.form.get('city')
    session['area'] = request.form.get('area')
    session['landmark'] = request.form.get('landmark')
    session['returnprovince'] = request.form.get('returnprovince')
    session['returncity'] = request.form.get('returncity')
    session['returnarea'] = request.form.get('returnarea')
    session['returnlandmark'] = request.form.get('returnlandmark')
    createSellerFolders(id)
    profile=request.files['userimg']
    front=request.files['cnicfrontside']
    back=request.files['cnicbackside']
    logo=request.files['brandlogo']
    saveImg(profile, './static/sellerData/'+id, 'profilePic')
    saveImg(front, './static/sellerData/'+id, 'front')
    saveImg(back, './static/sellerData/'+id, 'back')
    saveImg(logo, './static/sellerData/'+id, 'logo')
    session['userimg'] = '/sellerData/'+id+'/profilePic.'+ getImgExtensionByImgFilename(profile.filename)
    session['cnicfrontside'] = '/sellerData/'+id+'/front.'+getImgExtensionByImgFilename(front.filename)
    session['cnicbackside'] = '/sellerData/'+id+'/back.'+getImgExtensionByImgFilename(back.filename)
    session['brandlogo'] = '/sellerData/'+id+'/logo.'+getImgExtensionByImgFilename(logo.filename)


def addBuyerFromSession2DB():
    fname = session.get("firstname")
    lname = session.get("lastname")
    mail = session.get("email")
    uName = session.get("username")
    password = session.get("password")
    province = session.get('province')
    city = session.get('city')
    area = session.get('area')
    landmark = session.get('landmark')
    cnic = session.get("cnic")
    phNo = session.get("mobilenumber")
    id = session.get("userid")

    usr = User(user_id=id, email=mail, user_name=uName, password=password,
               cnic=cnic, first_name=fname, last_name=lname, is_active=True, contact_no=phNo)
    buy = Buyer(buyer_id=id, province=province,
                city=city, area=area, land_mark=landmark)
    seshion.add(usr)
    seshion.commit()
    seshion.add(buy)
    seshion.commit()


def addBuyerInSession(request):
    session['firstname'] = request.form["firstname"]
    session['lastname'] = request.form["lastname"]
    session['email'] = request.form["email"]
    session['username'] = request.form["username"]
    session['password'] = request.form["password"]
    session['province'] = request.form['province']
    session['city'] = request.form['city']
    session['area'] = request.form['area']
    session['landmark'] = request.form['landmark']
    session['cnic'] = request.form["cnic"]
    session['mobilenumber'] = request.form["mobilenumber"]
    session['userid'] = request.form["userid"]


def addSellerFromSession2DB():
    fname = session.get("firstname")
    lname = session.get("lastname")
    mail = session.get("email")
    uName = session.get("username")
    password = session.get("password")
    cnic = session.get("cnic")
    phNo = session.get("cntct")
    id = session.get("userid")
    usr = User(user_id=id, email=mail, user_name=uName, password=password,
               cnic=cnic, first_name=fname, last_name=lname, is_active=True, contact_no=phNo)

    s = Seller(seller_id=id, profile_pic=session['userimg'], cnic_front=session['cnicfrontside'],
               cnic_back=session['cnicbackside'], store_name=session['storename'], brand_logo=session['brandlogo'],
               pick_province=session['province'], pick_city=session['city'], pick_area=session['area'],
               pick_land_mark=session['landmark'], return_province=session['returnprovince'],
               return_city=session['returnprovince'], return_area=session['returnarea'],
               return_land_mark=session['returnlandmark'], bank_name='hbl', bank_account_no='12345678986543')
    seshion.add(usr)
    seshion.commit()
    print('before')
    seshion.add(s)
    seshion.commit()
    print('before')




def addIdInSession(id):
    session['id']=id


def getIdFromSession():
    return session.get('id')