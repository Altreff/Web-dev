export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}


export const products = [
  {
    id: 1,
    name: 'iPhone 14 Black',
    price: 799,
    rating: '4,6/5',
    link:'https://kaspi.kz/shop/p/apple-iphone-14-128gb-chernyi-106363023/',
    image: 'https://resources.cdn-kaspi.kz/img/m/p/h98/h2b/64400497737758.jpg?format=gallery-large',
    description: 'A large phone with one of the best screens',
    likes: 0,
    removes: true,
    prodcategory: 1

    
  
  },
  {
    id: 2,
    name: 'iPhone 13 Mini White',
    price: 699,
    rating: '4/5',
    link:'https://kaspi.kz/shop/p/apple-iphone-13-mini-128gb-belyi-102298521/',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hfc/h30/63998596677662.jpg?format=gallery-large',
    description: 'A great phone with one of the best cameras',
    removes: true,
    prodcategory: 1,
    likes: 0
  },
  {
    id: 3,
    name: 'iPhone 15 Pro Max Gray',
    price: 999,
    rating:'5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hc1/h65/83559848181790.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-seryi-113138420/',
    description: 'A new phone with one of the best performances',
    removes: true,
    prodcategory: 1,
    likes: 0
  },
  {
    id: 4,
    name: 'Samsung Galaxy A24',
    price: 399,
    rating:'5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hdc/h12/80750151303198.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/samsung-galaxy-a24-6-gb-128-gb-chernyi-110343531/?c=750000000',
    description: 'MediaTek Helio G99, 128GB',
    removes: true,
    prodcategory: 1,
    likes: 0
  },
  {
    id: 5,
    name: 'OPPO A18',
    price: 299,
    rating:'4/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h82/hc4/84434499960862.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/oppo-a18-4-gb-128-gb-chernyi-114291573/?c=750000000',
    description: 'Mediatek Helio G85, 128GB',
    removes: true,
    prodcategory: 1,
    likes: 0
  },
  {
    id: 6,
    name: 'Xiaomi Redmi Note 12',
    price: 199,
    rating:'5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hca/h10/79755729600542.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/xiaomi-redmi-note-12-6-gb-128-gb-seryi-109734268/?c=750000000',
    description: 'Qualcomm Snapdragon 685, 128GB',
    removes: true,
    prodcategory: 2,
    likes: 0
  },
  {
    id: 7,
    name: 'Xiaomi Redmi 9A',
    price: 99,
    rating:'4.5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hdf/hab/63754140450846.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/xiaomi-redmi-9a-2-gb-32-gb-seryi-100399600/?c=750000000',
    description: 'MediaTek Helio G25, 32GB',
    removes: true,
    prodcategory: 2,
    likes: 0
  },
  {
    id: 8,
    name: 'Nothing Phone 1',
    price: 199,
    rating:'5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h70/h46/64491278368798.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/nothing-phone-1-8-gb-256-gb-chernyi-106174998/?c=750000000',
    description: 'A new phone with one of the best performances',
    removes: true,
    prodcategory: 2,
    likes: 0
  },
  {
    id: 9,
    name: 'NOTHING Phone 2',
    price: 399,
    rating:'5/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h9d/h89/82543892234270.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/nothing-phone-2-12-gb-256-gb-chernyi-112351192/',
    description: 'Snapdragon 8+ Gen 1, 256GB',
    removes: true,
    prodcategory: 2,
    likes: 0
  },
  {
    id: 10,
    name: 'TECNO Spark 20 Pro',
    price: 999,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/he3/h3c/84810433593374.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/tecno-spark-20-pro-8-gb-256-gb-chernyi-115734827/?c=750000000',
    description: 'MediaTek Helio G99, 128GB',
    removes: true,
    prodcategory: 2,
    likes: 0
  },
  {
    id: 11,
    name: 'ASUS ROG Phone 8 Pro Edition',
    price: 999,
    rating:'4.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hd1/h16/85100427182110.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/asus-rog-phone-8-pro-edition-24-gb-1024-gb-chernyi-116452570/?c=750000000',
    description: 'Snapdragon 8 Gen 3, 1024 GB',
    removes: true,
    prodcategory: 3,
    likes: 0
  },
  {
    id: 12,
    name: 'Xiaomi Redmi Note 13 Pro 5G',
    price: 499,
    rating:'4/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hbb/h4a/85039724101662.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/xiaomi-redmi-note-13-pro-5g-12-gb-512-gb-sinii-116288022/?c=750000000',
    description: 'Snapdragon 7s Gen 2, 512GB',
    removes: true,
    prodcategory: 3,
    likes: 0
  },
  {
    id: 13,
    name: 'Samsung Galaxy S23 Ultra 5G',
    price: 799,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hdb/h1d/69067261116446.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/samsung-galaxy-s23-ultra-5g-12-gb-512-gb-zelenyi-108916042/?c=750000000',
    description: 'Snapdragon 8 Gen 2, 512GB',
    removes: true,
    prodcategory: 3,
    likes: 0
  },
  {
    id: 14,
    name: 'Poco M6 Pro',
    price: 899,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hfe/hdc/85032639528990.png?format=gallery-large',
    link:'https://kaspi.kz/shop/p/poco-m6-pro-12-gb-512-gb-fioletovyi-116265142/?c=750000000',
    description: 'Helio G99-Ultra, 512GB',
    removes: true,
    prodcategory: 3,
    likes: 0
  },
  {
    id: 15,
    name: 'Samsung Galaxy Z Flip5',
    price: 780,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h21/ha2/83172190617630.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/samsung-galaxy-z-flip5-8-gb-512-gb-seryi-112861648/?c=750000000',
    description: 'Qualcomm Snapdragon 8 Gen 2, 512GB',
    removes: true,
    prodcategory: 3,
    likes: 0
  },
  {
    id: 16,
    name: 'Itel IT2163 DS',
    price: 20,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hf7/hec/67160947916830.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/itel-it2163-ds-sinii-108160833/?c=750000000',
    description: '32MB',
    removes: true,
    prodcategory: 4,
    likes: 0
  },
  {
    id: 17,
    name: 'Nokia 106',
    price: 10,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h50/hd8/63778886516766.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/nokia-106-seryi-8800911/?c=750000000',
    description: '4MB',
    removes: true,
    prodcategory: 4,
    likes: 0
  },
  {
    id: 18,
    name: 'TeXet TM-D421',
    price: 999,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/hcc/h47/64489162407966.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/texet-tm-d421-chernyi-107221222/?c=750000000',
    description: '32MB',
    removes: true,
    prodcategory: 4,
    likes: 0
  },
  {
    id: 19,
    name: 'Nokia 130 2023 DS',
    price: 20,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h77/h99/84341934817310.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/nokia-130-2023-ds-sinii-114046351/?c=750000000',
    description: '4MB',
    removes: true,
    prodcategory: 4,
    likes: 0
  },
  {
    id: 20,
    name: 'Samsung SM-B310E',
    price: 10,
    rating:'3.9/5',
    image:'https://resources.cdn-kaspi.kz/img/m/p/h29/hc9/64444729229342.jpg?format=gallery-large',
    link:'https://kaspi.kz/shop/p/samsung-sm-b310e-chernyi-106602726/?c=750000000',
    description: '32MB',
    removes: true,
    prodcategory: 4,
    likes: 0
  }
  
];



/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/