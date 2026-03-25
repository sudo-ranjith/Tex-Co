const products = [
  {id:'p1',name:'Black Loopknit',type:'loopknit',gsm:180,color:'Jet Black',stock:420,price:82,grade:'A',comp:'100% Cotton',seller:'Karthik Textiles',sellerAv:'KT',rating:'4.8',orders:132,city:'Tiruppur',batch:'TXK-2024-882',defect:'Minor shade variation',emoji:'🧶',bg:'bg-green'},
  {id:'p2',name:'Navy Rib Fabric',type:'rib',gsm:220,color:'Navy Blue',stock:180,price:95,grade:'B',comp:'95% Cotton 5% Spandex',seller:'Sri Selvi Exports',sellerAv:'SS',rating:'4.5',orders:89,city:'Tiruppur',batch:'TXR-2024-441',defect:'Small holes',emoji:'🔷',bg:'bg-blue'},
  {id:'p3',name:'Cream Fleece',type:'fleece',gsm:300,color:'Off-White',stock:92,price:110,grade:'A',comp:'100% Polyester',seller:'Raja Fabrics',sellerAv:'RF',rating:'4.9',orders:204,city:'Erode',batch:'TXF-2024-207',defect:'Premium seconds',emoji:'✨',bg:'bg-yellow'},
  {id:'p4',name:'Red Interlock',type:'interlock',gsm:200,color:'Fire Red',stock:310,price:88,grade:'B',comp:'100% Cotton',seller:'Murugan Textiles',sellerAv:'MT',rating:'4.3',orders:67,city:'Tiruppur',batch:'TXI-2024-663',defect:'Color bleeding risk',emoji:'❤️',bg:'bg-red'},
  {id:'p5',name:'White Jersey',type:'jersey',gsm:160,color:'White',stock:560,price:72,grade:'A',comp:'100% Cotton',seller:'Priya Knits',sellerAv:'PK',rating:'4.7',orders:156,city:'Coimbatore',batch:'TXJ-2024-119',defect:'Minor pilling',emoji:'⬜',bg:'bg-gray'},
  {id:'p6',name:'Purple Interlock',type:'interlock',gsm:210,color:'Violet',stock:240,price:92,grade:'A',comp:'100% Cotton',seller:'Vignesh Fab Co',sellerAv:'VF',rating:'4.6',orders:98,city:'Tiruppur',batch:'TXI-2024-774',defect:'Texture variation',emoji:'💜',bg:'bg-purple'},
];

export default function handler(req, res) {
  if (req.method === 'GET') {
    const { id } = req.query;
    
    if (id) {
      const product = products.find(p => p.id === id);
      if (!product) {
        return res.status(404).json({ error: 'Product not found' });
      }
      return res.status(200).json(product);
    }
    
    return res.status(200).json(products);
  }
  
  res.status(405).json({ error: 'Method not allowed' });
}
