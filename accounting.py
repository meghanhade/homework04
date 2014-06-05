def main():

    import csv

    melon_cost = 1  
    
    for line in open("customer_orders.csv"):
        cust_num, name, expected_raw, paid_raw  = line.split(",")

        expected = int(expected_raw) * melon_cost
        paid_clean = float(paid_raw)
        paid = int(paid_clean)
        difference = expected - paid
        
        if expected != paid:
            print name, "paid $%r, expected $%r. There was a difference of $%r." % (paid, expected, difference)




if __name__ == "__main__":
    main()