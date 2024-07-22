a=['₹191₹99980% off\nFree delivery', '₹449₹1,49970% off\nFree delivery', '₹199₹99980% off\nFree delivery', '₹319₹1,29975% off\nFree delivery', '₹239₹99976% off\nFree delivery', '₹299₹1,99885% off\nFree delivery',
   '₹202₹99979% off\nFree delivery', '₹299₹1,09972% off\nFree delivery', '₹299₹1,29976% off\nFree delivery',
   '₹199₹99980% off\nFree delivery', '₹199₹99980% off\nFree delivery', '₹308₹1,09971% off\nFree delivery',
   '₹449₹1,49970% off\nFree delivery', '₹386₹1,49974% off\nFree delivery', '₹203₹99979% off\nFree delivery',
   '₹257₹99974% off\nFree delivery', '₹269₹99973% off\nFree delivery', '₹319₹1,09970% off\nFree delivery',
   '₹369₹1,89980% off\nFree delivery', '₹249₹99975% off\nFree delivery', '₹209₹1,49986% off\nFree delivery',
   '₹437₹1,89976% off\nFree delivery', '₹319₹1,29975% off\nFree dlivery', '₹449₹1,49970% off\nFree delivery',
   '₹213₹99978% off\nFree delivery', '₹645₹2,29971% off\nFree delivery', '₹320₹1,29975% off\nFree delivery',
   '₹229₹1,99988% off\nFree delivery', '₹305₹1,09972% off\nFree delivery', '₹299₹1,29976% off\nFree delivery',
   '₹289₹1,59981% off\nFree delivery', '₹299₹99970% off\nFree delivery', '₹319₹1,29975% off\nFree delivery',
   '₹456₹1,89975% off\nFree delivery', '₹279₹99972% off\nFree delivery', '₹241₹1,49983% off\nFree delivery',
   '₹269₹99973% off\nFree delivery', '₹418₹1,89977% off\nFree delivery', '₹269₹99973% off\nFree delivery',
   '₹265₹88870% off\nFree delivery']

import re

for i in range(len(a)):
   split=a[i].split()[0]
   matches = ''.join(re.findall('(\d{2})%', split))
   print(matches)

