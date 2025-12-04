prices = [100, 50, 30]       
qty = [2, 1, 3]             
disc_pct = 10                
tax_pct = 5                  

sub = sum(p*q for p, q in zip(prices, qty))
disc_amt = sub * disc_pct / 100
sub_after_disc = sub - disc_amt
tax_amt = sub_after_disc * tax_pct / 100
total = sub_after_disc + tax_amt

print("Subtotal:", sub)
print("Discount:", disc_amt)
print("After Discount:", sub_after_disc)
print("Tax:", tax_amt)
print("Total Bill:", total)
