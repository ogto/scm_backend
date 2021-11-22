from app import db


class Category(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_no = db.Column(db.Integer)
    category_depth = db.Column(db.Integer, nullable=False, default=1)
    parent_category_no = db.Column(db.Integer)
    category_name = db.Column(db.String(50))
    display_type = db.Column(db.String(1))
    full_category_no = db.Column(db.String(8))
    full_category_name = db.Column(db.String(250))
    use_main = db.Column(db.String(1), default='F')
    use_display = db.Column(db.String(1), default='F')
    display_order = db.Column(db.Integer, nullable=False, default=1)
    soldout_product_display = db.Column(db.String(1))
    sub_category_product_display = db.Column(db.String(1), nullable=False, default='F')
    hashtag_product_display = db.Column(db.String(1), nullable=False, default='T')
    product_display_scope = db.Column(db.String(1), nullable=False, default='A')
    product_display_type = db.Column(db.String(1), nullable=False, default='U')
    product_display_key = db.Column(db.String(1), nullable=False, default='A')
    product_display_sort = db.Column(db.String(1), nullable=False, default='D')
    product_display_period = db.Column(db.String(1), nullable=False, default='W')
    normal_product_display_type = db.Column(db.String(1), nullable=True)
    normal_product_display_key = db.Column(db.String(1), nullable=True)
    normal_product_display_sort = db.Column(db.String(1), nullable=True)
    normal_product_display_period = db.Column(db.String(1), nullable=True)
    recommend_product_display_type = db.Column(db.String(1), nullable=True)
    recommend_product_display_key = db.Column(db.String(1), nullable=True)
    recommend_product_display_sort = db.Column(db.String(1), nullable=True)
    recommend_product_display_period = db.Column(db.String(1), nullable=True)
    new_product_display_type = db.Column(db.String(1), nullable=True)
    new_product_display_key = db.Column(db.String(1), nullable=True)
    new_product_display_sort = db.Column(db.String(1), nullable=True)
    new_product_display_period = db.Column(db.String(1), nullable=True)
    access_authority = db.Column(db.String(1), nullable=False, default='T')
