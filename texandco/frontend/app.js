// Tex & Co Frontend - Complete Working Version

const PRODUCTS = [
  {id:'p1',name:'Black Loopknit',type:'loopknit',gsm:180,color:'Jet Black',stock:420,price:82,grade:'A',comp:'100% Cotton',seller:'Karthik Textiles',sellerAv:'KT',rating:'4.8',orders:132,city:'Tiruppur',batch:'TXK-2024-882',defect:'Minor shade variation',emoji:'🧶',bg:'bg-green'},
  {id:'p2',name:'Navy Rib Fabric',type:'rib',gsm:220,color:'Navy Blue',stock:180,price:95,grade:'B',comp:'95% Cotton 5% Spandex',seller:'Sri Selvi Exports',sellerAv:'SS',rating:'4.5',orders:89,city:'Tiruppur',batch:'TXR-2024-441',defect:'Small holes',emoji:'🔷',bg:'bg-blue'},
  {id:'p3',name:'Cream Fleece',type:'fleece',gsm:300,color:'Off-White',stock:92,price:110,grade:'A',comp:'100% Polyester',seller:'Raja Fabrics',sellerAv:'RF',rating:'4.9',orders:204,city:'Erode',batch:'TXF-2024-207',defect:'Premium seconds',emoji:'✨',bg:'bg-yellow'},
  {id:'p4',name:'Red Interlock',type:'interlock',gsm:200,color:'Fire Red',stock:310,price:88,grade:'B',comp:'100% Cotton',seller:'Murugan Textiles',sellerAv:'MT',rating:'4.3',orders:67,city:'Tiruppur',batch:'TXI-2024-663',defect:'Color bleeding risk',emoji:'❤️',bg:'bg-red'},
  {id:'p5',name:'White Jersey',type:'jersey',gsm:160,color:'White',stock:560,price:72,grade:'A',comp:'100% Cotton',seller:'Priya Knits',sellerAv:'PK',rating:'4.7',orders:156,city:'Coimbatore',batch:'TXJ-2024-119',defect:'Minor pilling',emoji:'⬜',bg:'bg-gray'},
  {id:'p6',name:'Purple Interlock',type:'interlock',gsm:210,color:'Violet',stock:240,price:92,grade:'A',comp:'100% Cotton',seller:'Vignesh Fab Co',sellerAv:'VF',rating:'4.6',orders:98,city:'Tiruppur',batch:'TXI-2024-774',defect:'Texture inconsistency',emoji:'💜',bg:'bg-purple'},
];

const CATEGORIES = [
  {name:'Loopknit',emoji:'🧶'},
  {name:'Jersey',emoji:'⬜'},
  {name:'Rib',emoji:'🔷'},
  {name:'Fleece',emoji:'✨'},
  {name:'Interlock',emoji:'❤️'},
];

const ORDERS = [
  {buyer:'Ravi Garments',product:'Black Loopknit',qty:'120 kg',amt:'₹9,840',status:'transit',emoji:'🧶',bg:'bg-green'},
  {buyer:'Sri Selvi Exports',product:'Red Interlock',qty:'80 kg',amt:'₹7,040',status:'placed',emoji:'❤️',bg:'bg-red'},
  {buyer:'Murugan Fab',product:'Navy Rib Fabric',qty:'60 kg',amt:'₹5,700',status:'delivered',emoji:'🔷',bg:'bg-blue'},
  {buyer:'Priya Knits',product:'Cream Fleece',qty:'40 kg',amt:'₹4,400',status:'processing',emoji:'✨',bg:'bg-yellow'},
  {buyer:'Senthil & Co',product:'White Jersey',qty:'200 kg',amt:'₹14,400',status:'delivered',emoji:'⬜',bg:'bg-gray'},
  {buyer:'ABCTextiles',product:'Purple Interlock',qty:'100 kg',amt:'₹9,200',status:'transit',emoji:'💜',bg:'bg-purple'},
];

const STATUS_MAP = {transit:'In Transit',placed:'New Order',delivered:'Delivered',processing:'Processing',cancelled:'Cancelled'};
const STATUS_CLASS = {transit:'st-transit',placed:'st-placed',delivered:'st-delivered',processing:'st-processing',cancelled:'st-cancelled'};

let cart = [];
let currentDetailProduct = null;
let detailFromScreen = 'home';

function safeFormat(num) {
  try {
    if (num === undefined || num === null || isNaN(num)) return '₹0';
    return '₹' + parseInt(num).toLocaleString('en-IN');
  } catch (e) {
    return '₹0';
  }
}

function updateTotals() {
  try {
    let subTotal = 0;
    if (cart && cart.length > 0) {
      cart.forEach(item => {
        subTotal += (item.qty || 0) * (item.price || 0);
      });
    }
    const gstAmount = Math.round(subTotal * 0.05);
    const total = subTotal + 850 + gstAmount;
    const e1 = document.getElementById('subtotal');
    const e2 = document.getElementById('gst-amt');
    const e3 = document.getElementById('total-amt');
    if (e1) e1.textContent = safeFormat(subTotal);
    if (e2) e2.textContent = safeFormat(gstAmount);
    if (e3) e3.textContent = safeFormat(total);
  } catch (e) {
    console.error('updateTotals error:', e);
  }
}

function renderCart() {
  try {
    const list = document.getElementById('cart-list');
    if (!list) return;
    if (!cart || cart.length === 0) {
      list.innerHTML = '<div class=\"empty-state\"><div class=\"empty-icon\">🛒</div><div class=\"empty-title\">Cart empty</div></div>';
      const c = document.getElementById('cart-count');
      if (c) c.textContent = '0 items';
      updateTotals();
      return;
    }
    let h = '';
    cart.forEach((it, i) => {
      h += '<div class=\"cart-item\"><div class=\"cart-img ' + it.bg + '\">' + it.emoji + '</div><div class=\"cart-info\"><div class=\"cart-name\">' + it.name + '</div><div class=\"cart-spec\">' + it.qty + 'kg @ ₹' + it.price + '/kg</div><div class=\"cart-price\">' + safeFormat(it.qty * it.price) + '</div></div><div class=\"qty-ctrl\"><button class=\"qty-btn\" onclick=\"updateQty(' + i + ', -50)\">−</button><div class=\"qty-val\">' + it.qty + 'kg</div><button class=\"qty-btn\" onclick=\"updateQty(' + i + ', 50)\">+</button></div></div>';
    });
    list.innerHTML = h;
    const c = document.getElementById('cart-count');
    if (c) c.textContent = cart.length + ' item' + (cart.length > 1 ? 's' : '');
    updateTotals();
  } catch (e) {
    console.error('renderCart error:', e);
  }
}

function updateQty(i, d) {
  try {
    if (cart[i]) {
      cart[i].qty = Math.max(50, cart[i].qty + d);
      renderCart();
    }
  } catch (e) {
    console.error('updateQty error:', e);
  }
}

function renderProducts(id, list) {
  try {
    const c = document.getElementById(id);
    if (!c) return;
    let h = '';
    const fromScreen = id === 'search-grid' ? 'search' : (id === 'wishlist-grid' ? 'wishlist' : 'home');
    list.forEach(p => {
      h += '<div class=\"product-card\" onclick=\"showDetail(\'' + p.id + '\', \'' + fromScreen + '\')\"><div class=\"product-img ' + p.bg + '\">' + p.emoji + '</div><div class=\"product-body\"><div class=\"product-name\">' + p.name + '</div><div class=\"product-spec\">' + p.color + ' • ' + p.gsm + 'gsm</div><div class=\"product-foot\"><div class=\"product-price\">' + safeFormat(p.price) + '</div><div class=\"grade-tag grade-' + p.grade.toLowerCase() + '\">' + p.grade + '</div></div></div></div>';
    });
    c.innerHTML = h;
  } catch (e) {
    console.error('renderProducts error:', e);
  }
}

function renderOrders(id) {
  try {
    const c = document.getElementById(id);
    if (!c) return;
    let h = '';
    ORDERS.forEach(o => {
      h += '<div class=\"order-row\"><div class=\"order-thumb ' + o.bg + '\">' + o.emoji + '</div><div class=\"order-info\"><div class=\"order-buyer\">' + o.buyer + '</div><div class=\"order-detail\">' + o.product + ' • ' + o.qty + '</div></div><div class=\"status-pill ' + STATUS_CLASS[o.status] + '\">' + STATUS_MAP[o.status] + '</div></div>';
    });
    c.innerHTML = h;
  } catch (e) {
    console.error('renderOrders error:', e);
  }
}

function renderCategories() {
  try {
    const c = document.getElementById('categories');
    if (!c) return;
    let h = '';
    CATEGORIES.forEach((cat, i) => {
      h += '<div class="cat-chip ' + (i === 0 ? 'active' : '') + '" onclick="filterCat(this, \'' + cat.name.toLowerCase() + '\')" style="cursor:pointer;"><div class="cat-icon">' + cat.emoji + '</div><div class="cat-label">' + cat.name + '</div></div>';
    });
    c.innerHTML = h;
  } catch (e) {
    console.error('renderCategories error:', e);
  }
}

function showScreen(s) {
  try {
    document.querySelectorAll('.screen').forEach(x => x.classList.remove('active'));
    const el = document.getElementById('screen-' + s);
    if (el) el.classList.add('active');
  } catch (e) {
    console.error('showScreen error:', e);
  }
}

function goBack() {
  try {
    switchNav(detailFromScreen);
  } catch (e) {
    console.error('goBack error:', e);
  }
}

function showDetail(pid, from) {
  try {
    const p = PRODUCTS.find(x => x.id === pid);
    if (!p) return;
    currentDetailProduct = p;
    detailFromScreen = from || 'home';
    
    // Populate detail page
    const n = document.getElementById('detail-name');
    const pr = document.getElementById('detail-price');
    const img = document.getElementById('detail-img');
    const seller = document.getElementById('detail-seller');
    
    if (n) n.textContent = p.name;
    if (pr) pr.textContent = safeFormat(p.price);
    if (img) img.innerHTML = '<div style="width:100%;height:240px;background:' + (p.bg === 'bg-green' ? '#D4F1E8' : p.bg === 'bg-blue' ? '#D9E8F5' : p.bg === 'bg-yellow' ? '#FDF3E1' : p.bg === 'bg-red' ? '#FFE0E0' : p.bg === 'bg-purple' ? '#F3E0FF' : '#F0F0F0') + ';display:flex;align-items:center;justify-content:center;font-size:120px;">' + p.emoji + '</div>';
    if (seller) seller.textContent = p.seller;
    
    showScreen('detail');
  } catch (e) {
    console.error('showDetail error:', e);
  }
}

function addToCart() {
  try {
    if (!currentDetailProduct) return;
    const p = currentDetailProduct;
    const ex = cart.find(c => c.id === p.id);
    if (ex) {
      ex.qty += 50;
    } else {
      cart.push({id: p.id, name: p.name, qty: 50, price: p.price, emoji: p.emoji, bg: p.bg});
    }
    renderCart();
  } catch (e) {
    console.error('addToCart error:', e);
  }
}

function switchNav(s) {
  try {
    // Remove 'screen-' prefix if present
    const screenName = s.replace('screen-', '');
    
    // Show the screen
    showScreen(screenName);
    
    // If switching to search, populate and focus
    if (screenName === 'search') {
      setTimeout(() => {
        const searchInput = document.querySelector('#screen-search input[type="text"]');
        if (searchInput) {
          searchInput.focus();
          searchInput.value = '';
          doSearch('');
        }
      }, 50);
    }
    
    // Update nav highlighting
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
    const navMap = {
      'home': 0,
      'search': 1,
      'cart': 2,
      'seller': 3,
      'profile': 4
    };
    
    const navIndex = navMap[screenName];
    if (navIndex !== undefined) {
      const navItems = document.querySelectorAll('.nav-item');
      if (navItems[navIndex]) {
        navItems[navIndex].classList.add('active');
      }
    }
  } catch (e) {
    console.error('switchNav error:', e);
  }
}

function filterCat(el, cat) {
  try {
    document.querySelectorAll('.cat-chip').forEach(e => e.classList.remove('active'));
    el.classList.add('active');
    const filtered = PRODUCTS.filter(p => p.type.toLowerCase() === cat.toLowerCase());
    renderProducts('product-grid', filtered);
  } catch (e) {
    console.error('filterCat error:', e);
  }
}

function renderWishlist() {
  try {
    const w = document.getElementById('wishlist-grid');
    if (w) {
      renderProducts('wishlist-grid', PRODUCTS.slice(0, 3));
    }
  } catch (e) {
    console.error('renderWishlist error:', e);
  }
}

function doSearch(val) {
  try {
    let results = PRODUCTS;
    if (val && val.trim()) {
      results = results.filter(p => p.name.toLowerCase().includes(val.toLowerCase()) || p.color.toLowerCase().includes(val.toLowerCase()));
    }
    renderProducts('search-grid', results);
    const cnt = document.getElementById('result-count');
    if (cnt) {
      if (results.length === 0) {
        cnt.textContent = 'No products found';
      } else {
        cnt.textContent = results.length + ' product' + (results.length > 1 ? 's' : '') + ' found';
      }
    }
  } catch (e) {
    console.error('doSearch error:', e);
  }
}

function openUploadModal() {
  try {
    const m = document.getElementById('modal-upload');
    if (m) m.classList.add('open');
  } catch (e) {
    console.error('openUploadModal error:', e);
  }
}

function openCheckout() {
  try {
    updateTotals();
    const total = document.getElementById('total-amt');
    if (total) {
      const ct = document.getElementById('checkout-total');
      if (ct) ct.textContent = total.textContent;
    }
    const m = document.getElementById('modal-checkout');
    if (m) m.classList.add('open');
  } catch (e) {
    console.error('openCheckout error:', e);
  }
}

function closeModal() {
  try {
    document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
  } catch (e) {
    console.error('closeModal error:', e);
  }
}

function submitUpload() {
  try {
    closeModal();
  } catch (e) {
    console.error('submitUpload error:', e);
  }
}

function placeOrder() {
  try {
    closeModal();
    cart = [];
    renderCart();
    showScreen('home');
  } catch (e) {
    console.error('placeOrder error:', e);
  }
}

function initializeApp() {
  try {
    // Initialize nav with home active
    const homeNav = document.querySelector('.nav-item');
    if (homeNav) homeNav.classList.add('active');
    
    // Render all content
    renderCategories();
    renderProducts('product-grid', PRODUCTS);
    renderProducts('search-grid', PRODUCTS);
    renderWishlist();
    renderOrders('seller-orders');
    renderCart();
    
    // Setup modal close on overlay click
    document.querySelectorAll('.modal-overlay').forEach(m => {
      m.addEventListener('click', function(e) {
        if (e.target === this) closeModal();
      });
    });
    
    // Add click handlers to notification and wishlist icons
    const topbarIcons = document.querySelectorAll('.topbar-icons .icon-btn');
    if (topbarIcons[0]) {
      topbarIcons[0].addEventListener('click', function() {
        switchNav('notifications');
      });
    }
    if (topbarIcons[1]) {
      topbarIcons[1].addEventListener('click', function() {
        switchNav('wishlist');
      });
    }
    
    console.log('✅ App ready!');
  } catch (e) {
    console.error('Init error:', e);
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}
