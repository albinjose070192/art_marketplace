import datetime

class Art:
  def __init__(self,artist,title,year,medium,owner=''):
    self.artist=artist
    self.title=title
    self.medium=medium
    self.year=year
    self.owner=owner
    
  def __repr__(self):
   return "{}. \"{}\". {}, {}\n{}, {}".format(self.artist,self.title,self.year,self.medium,self.owner.name,self.owner.location)

class Marketplace:
  def __init__(self,listings):
    self.listings=listings
  
  def add_listing(self,new_listing):
    self.listings.append(new_listing)
    return self.listings
  
  def remove_listing(self,listing):
    self.listings.remove(listing)
    return self.listings
  
  def show_listings(self):
    for art in self.listings:
      if datetime.date.today()<art.expiry_date:
        print(art)
      print("\n")
    return None

class Client:
  def __init__(self,name,location,is_museum,wishlist, wallet=0):
    self.name=name
    self.location=location
    self.is_museum=is_museum
    self.wallet=wallet
    self.wishlist=wishlist

  def add_to_wishlist(self,art):
    for art_listing in veneer.listings:
      if art.owner!=self:
        if art.title in art_listing.art.title:
          self.wishlist.append(art) 
        else:
          pass
    return self.wishlist

  #Adds money in your wallet in Million USD
  def add_wallet(self,amount):
    self.wallet+=amount
    return self.wallet

  def sell_artwork(self,artwork,price,expiry_date):
    if artwork.owner==self:
      artwork_for_sale=Listing(artwork,price,artwork.owner,expiry_date)
      veneer.add_listing(artwork_for_sale)
  
  def buy_artwork(self,artwork):
    if artwork.owner!=self:
      for art_listing in veneer.listings:
        if self.wallet>=art_listing.price:
          if artwork.title in art_listing.art.title:
            art_listing.seller.wallet+=art_listing.price
            artwork.owner=self
            self.wallet=self.wallet-art_listing.price
            veneer.remove_listing(art_listing)
        else:
          print("Your Wallet does not have sufficient balance to make this transaction. Please add money in your wallet to make the purchase.\n")
    return veneer.listings
  
class Listing:
  def __init__(self,art,price,seller,expiry_date):
    self.art=art
    self.price=price
    self.seller=seller
    self.expiry_date=expiry_date
  
  def __repr__(self):
    return "{}, ${}M USD".format(self.art, self.price)
  


veneer=Marketplace([])

edytta=Client("Edytta Halpirt","Private Collection",False,[])
moma=Client("The MOMA","New York",True,[])

girl_with_mandolin=Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)","1910","oil on canvas",edytta)  

vétheuil_in_the_fog=Art("Monet, Claude","Vétheuil in the Fog","1879","oil on canvas",edytta)

edytta.sell_artwork(girl_with_mandolin,6,datetime.date(2020,5,29))

edytta.sell_artwork(vétheuil_in_the_fog,20,datetime.date(2020,5,27))

moma.add_wallet(10)

moma.buy_artwork(girl_with_mandolin)

moma.sell_artwork(girl_with_mandolin,25,datetime.date(2020,5,30))

veneer.show_listings()


moma.add_to_wishlist(vétheuil_in_the_fog)

edytta.add_to_wishlist(girl_with_mandolin)
