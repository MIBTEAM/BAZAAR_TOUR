from .resources import AddInWishList, AddToCart, GetCartProducts, GetProducts, GetWishListProducts, getProductsSpecification, getReviewsByProductId


def initialize_routes(api):
    api.add_resource(GetProducts, '/getProducts')
    api.add_resource(AddInWishList, '/addInWishList/<p_id>')
    api.add_resource(GetWishListProducts,'/getWishListProducts')
    api.add_resource(AddToCart,'/addToCart/<p_id>')
    api.add_resource(GetCartProducts,'/getCartProducts')
    api.add_resource(getReviewsByProductId,'/getReviewsByProductId/<p_id>')
    api.add_resource(getProductsSpecification,'/getProductsSpecification')
