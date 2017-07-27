import csv



li = [];
delete = [];
temp = -1;

with open("number.csv","rb") as f:
	read = csv.reader(f);
	for i in list(read)[0]:

		temp=temp+1;
		d = {};
		if(i== ""):
			if(temp%2 == 0):
				delete.append(temp);
			else:
				d['id']=temp;
		else:
			d['id'] = int(i);
		if(len(d.keys())>0):
			li.append(d);

size = temp - len(delete);
temp=-1;
with open("fruits.csv","rb") as f:
	read = csv.reader(f);
	for N in li(read)[0]:
		temp=temp+1;
		if temp not in delete:
			for d in li:
				if(d['id']==temp):
					d['name']=N;
					print(d['N'])
	i=1;
	for d in li:
		if(d['N']==""):
			d['N'] = li[(i - 10)%size]['name']
		i=i+1;
temp = -1
with open("price.csv","rb") as f:
	read = csv.reader(f)
  for price in li(read)[0]:
  		temp = temp + 1;
  		for d in li:
  			if(d['id']== temp):
  				if(price == ""):
  					price = 0.0
  				else:
  					price = float(price)
  				d['price'] = price
  temp = -1

with open("rotten.csv","rb") as f:
	read = csv.reader(f)
	for rotten in list(read)[0]:
		temp=temp+1
		for d in li:
			if(d['id']== temp):
				if(rot == "0"):
					rot = "F"
				if(rot == "1"):
					rot = "T"
				if(rot == "T"):
					d['price']=0.0
				d['rot'] = rot



with open("DATA.csv","rb") as f:
	  d1 = csv.DictWriter(f,fieldnames = ['ID','NAME','PRICE','ROTTEN']);
	d1.writeheader();
	for d in li:
		d1.writerow(d);
