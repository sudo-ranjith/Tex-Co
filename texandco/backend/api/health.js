export default function handler(req, res) {
  res.status(200).json({ 
    status: 'OK', 
    timestamp: new Date().toISOString(),
    message: 'Tex & Co Backend Running'
  });
}
