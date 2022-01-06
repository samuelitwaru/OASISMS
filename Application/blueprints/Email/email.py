from flask import Blueprint, render_template, url_for, request, redirect, flash
from Application.database.model import Email, Sale, Purchase, KitchenStockPurchase
import datetime
from flask_login import current_user, login_required
from flask_mail import Message
from Application import mail
from Application.blueprints import utils


email = Blueprint('email', __name__, url_prefix="/email")


@email.route("/send-email")
@login_required
def send_email():
    # check the last time an email was sent. if the duration is
    # above 7 days, then send an email. else do nothing
    latest_email, date = Email.get_latest(Email)
    duration = datetime.timedelta(0)
    if latest_email:
        today = datetime.datetime.now()
        duration = today - date
    if duration > datetime.timedelta(7):
        # get sales
        sales = Sale.filter(Sale, "all", "", "", date, datetime.datetime(9999, 12, 31))
        total_sales = utils.compute_sales(sales)
        # get purchases
        kitchen_purchases = KitchenStockPurchase.filter2(KitchenStockPurchase, "", date, datetime.datetime(9999, 12, 31), True)
        brand_purchases = Purchase.filter(Purchase, "", date, datetime.datetime(9999, 12, 31), True)
        total_purchases = KitchenStockPurchase.get_total_price(KitchenStockPurchase, purchases=kitchen_purchases) + Purchase.get_total_price(Purchase, purchases=brand_purchases)

        # get boss' email address
        boss_email = current_user.manager.boss_email
        # send email
        msg = Message("Weekly sales and purchases", sender='samuelitwaru@gmail.com', recipients=[boss_email])
        msg.html = render_template('manager/sales_and_purchases_email.html', sales=sales, kitchen_purchases=kitchen_purchases, brand_purchases=brand_purchases, total_sales=total_sales, total_purchases=total_purchases, date=date)
        try:
            mail.send(msg)
            Email()
        except:
            flash("Failed to send Email!", "warning")
    return redirect(url_for('user.login'))