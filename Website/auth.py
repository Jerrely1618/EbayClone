#Login/Sign_up pages

from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import UserApplication,Items as ItemsListed,Users,Reports,Complaints
from . import db
import base64 #src = https://stackoverflow.com/questions/2323128/convert-string-in-base64-to-image-and-save-on-filesystem
verify_page = Blueprint('verify_page',__name__)

@verify_page.route('/browser/<username>',methods=['POST','GET'])
def browser(username):
    user = Users.query.filter_by(email=username).first()
    if request.method=="POST":
        searchItem = request.form["searchItem"]
        itemsList = ItemsListed.query.filter_by(title=searchItem).order_by(ItemsListed.time)
        return render_template("browser.html",items=itemsList,user=user,inputSearch=searchItem)
    itemsList = ItemsListed.query.order_by(ItemsListed.time)
    return render_template("browser.html",items=itemsList,user=user)

@verify_page.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        users = Users.query.filter_by(email=username)
        for user in users:  
            if user.password != password:
                flash("User or password do not matched with any of our records")   
            else:
                return redirect('/browser/'+username)
        flash("User or password do not matched with any of our records")
    # username = "random89@gmail.com"
    # password = "random89"
    # name = "Randy"
    # phone = "213809128645463"
    # creditcard="3213124121"
    # address = "Brooklyna"
    # tryUser = Users(name=name,email=username,phone=phone,credit_card=creditcard,address=address,password=password)
    # db.session.add(tryUser)
    # db.session.commit()
    return render_template("login.html")

@verify_page.route('/item/<titleName>',methods=['POST','GET'])
def item(titleName):
    item = ItemsListed.query.filter_by(title=titleName).first()
    image = base64.b64encode(item.img).decode('ascii')
    if request.method == "POST":
        newReport = Reports(title=item.title,description = request.form["description"],user_complainer="Guest")
        db.session.add(newReport)
        db.session.commit()
        flash("Reported.",category="success")
    return render_template("item.html",item=item,img = image)

@verify_page.route('/item/<titleName>/<username>',methods=['POST','GET'])
def itemUser(titleName,username):
    user = Users.query.filter_by(email=username).first()
    it = ItemsListed.query.filter_by(title=titleName).first()
    image = base64.b64encode(it.img).decode('ascii')
    if request.method == "POST":
        if request.form["submit"] == "Bid":
            if (float)(it.price) < (float)(request.form["bid"]):
                it.price = request.form["bid"]
                it.userBidder = user.email
                db.session.commit()
                flash("Bid of $"+request.form["bid"]+" submitted",category = "success")
            else:
                flash("Too little.",category="error")
        elif request.form["submit"] == "Report Item":
            newReport = Reports(title=it.title,description = request.form["description"],user_complainer=user.email)
            db.session.add(newReport)
            db.session.commit()
            flash("Reported.",category="success")
        elif request.form["submit"]=="Sell":
            db.session.delete(it)
            db.session.commit()
            flash("Item sold.",category = "success")
            return redirect("/browser/"+user.email)
        else:
            newComplaint = Complaints(user=it.user,description=request.form["description"],user_complainer=user.email)
            db.session.add(newComplaint)
            db.session.commit()
            flash("Complaint Submitted.",category="success")
    return render_template("itemUser.html",item=it,img=image,user=user)

@verify_page.route('/newItem/<username>',methods=['POST','GET'])
def itemInput(username):
    user = Users.query.filter_by(email=username).first()
    if request.method=="POST":
        title = request.form.get('title')
        price = request.form.get('price')
        desc = request.form.get('keywords')
        image = request.files['image']
        buyerDummy = "Dummy"
        newItem = ItemsListed(img=image.read(),user_bidder=buyerDummy,title=title,user=user.email,keywords=desc,price=price)
        db.session.add(newItem)
        db.session.commit()
    return render_template('inputItem.html',user=user)
    
@verify_page.route('/admin',methods=['POST','GET'])
def admin():
    def ProcessApplications()->None:
        for application in guestApplication:
           if (application.requirements == True):
               Users.append(application.user)
             

    def ProcessItems()->None:
        for application in ItemApplication:
            if (application.requirements == True):
               ItemsListed.append(application.item)
    

    def WarnUser(user)->None:	
       if(Users.complaints>=1):
          print('User warned')
    

    def Statistics()->None:
        reportsComplaints = len(reportsComplaints)
        usersTotal = len(Users)
        itemsApplications = len(itemsApplications)
        itemsTotal = len(items)
        userApplications = len(userApplications)
        print("Total Users: " + usersTotal + "Total items: " + itemsTotal + "Total user applications: "
         + userApplications + "Total item applications: " + itemsApplications)
    return render_template("admin.html")
    
 
@verify_page.route('/account/<username>',methods=['POST','GET'])
def account(username):
    user = Users.query.filter_by(email=username).first()
    return render_template("account.html",user=user)
    def changeBalance(user):
        quantity = 1

    def submitItem():
        picture = ' '
        title = ' '
        keyWords = ' '
        time = ''
        price = ''

         

    def submitBid(item, user):
        bid = input("Enter Bid: ")
    

    def complaint(user):
        complaintInfo = input("Enter your complaint: ")

    def rate(user):
        rating = input("Enter rating between 1 & 5: ")

    def transactionHistory():
        transactionDict = {item1: price1, item2: price2}
        print(transactionDict[i])

    def accountInfo(user):
        userPassword = input("Enter Password: ")
        userName = input("Enter Name: ")
        userAddress = input("Enter Address: ")
        userPhone = input(" Enter Phone Number: ")
        userCreditCardNumber = input("Enter Credit Card Number: ")
        
        print("Password: " + userPassword + "Name: " + userName + "Address: "
        + userAddress + "Phone: " + userPhone + "Credit Card Number: "
        + userCreditCardNumber)

    def changeInfo():
        newPassword = input("Enter New Password: ")
        newPassword = userPassword

        newName = input("Enter New Name: ")
        newName = userName

        newAddress = input("Enter New Address: ")
        newAddress = userAddress

        newPhone = input("Enter New Phone Number: ")
        newPhone = userPhone

        newCreditCardNumber = input("Enter New Credit Card Number: ")
        newCreditCardNumber = userCreditCardNumber



    
    return render_template("account.html")

@verify_page.route('/sign-up',methods=['POST','GET'])
def sign_up():
    if request.method=="POST":
        username = request.form['name']
        email = request.form['email']
        VerifiedEmail = request.form['email_ver']
        Password = request.form['password']
        VerifiedPassword = request.form['password_ver']
        phoneNum = request.form['phone']
        address = request.form['address']
        creditCard = request.form['Credit_card']
        if len(username) < 3:
            flash("Name should be at least 3 characters",category="error")
        elif email != VerifiedEmail or len(email)<3:
            flash("Emails do not match.",category="error")
        elif Password != VerifiedPassword:
            flash("Passwords do not match.",category="error")
        elif len(Password) < 7:
            flash("Passsword is too short.",category="error")
        else:             
            newGuestApp = UserApplication(name=username,email=email,password=Password,address=address,phone=phoneNum,credit_card=creditCard)
            db.session.add(newGuestApp)
            db.session.commit()
            flash("Application sent",category="Sucess")
            return redirect(url_for("pages.home"))
    return render_template("sign-up.html")