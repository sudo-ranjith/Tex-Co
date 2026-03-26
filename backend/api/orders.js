const orders = [
  {id:'o1',buyer:'Ravi Garments',product:'Black Loopknit',qty:'120 kg',amt:'₹9,840',status:'transit',emoji:'🧶',bg:'bg-green'},
  {id:'o2',buyer:'Sri Selvi Exports',product:'Red Interlock',qty:'80 kg',amt:'₹7,040',status:'placed',emoji:'❤️',bg:'bg-red'},
  {id:'o3',buyer:'Murugan Fab',product:'Navy Rib Fabric',qty:'60 kg',amt:'₹5,700',status:'delivered',emoji:'🔷',bg:'bg-blue'},
  {id:'o4',buyer:'Priya Knits',product:'Cream Fleece',qty:'40 kg',amt:'₹4,400',status:'processing',emoji:'✨',bg:'bg-yellow'},
  {id:'o5',buyer:'Senthil & Co',product:'White Jersey',qty:'200 kg',amt:'₹14,400',status:'delivered',emoji:'⬜',bg:'bg-gray'},
  {id:'o6',buyer:'ABCTextiles',product:'Purple Interlock',qty:'100 kg',amt:'₹9,200',status:'transit',emoji:'💜',bg:'bg-purple'},
];

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', 'true')
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version')
  
  if (req.method === 'OPTIONS') {
    res.status(200).end()
    return
  }

  if (req.method === 'GET') {
    return res.status(200).json(orders);
  }

  if (req.method === 'POST') {
    const { company, email, address, total, items } = req.body;
    
    if (!company || !email || !address || !items) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const order = {
      id: 'o' + Date.now(),
      company,
      email,
      address,
      total,
      items,
      status: 'placed',
      createdAt: new Date().toISOString()
    };

    return res.status(201).json({ message: 'Order created successfully', order });
  }

  res.status(405).json({ error: 'Method not allowed' });
}
