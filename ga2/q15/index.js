const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());
app.post('/data', (req, res) => {
    const { type, value } = req.body;
    let reversed;
    if (type === 'string') reversed = value.split('').reverse().join('');
    else if (type === 'array') reversed = [...value].reverse();
    else if (type === 'words') reversed = value.split(' ').reverse().join(' ');
    else if (type === 'number') reversed = parseInt(value.toString().split('').reverse().join(''));
    res.json({ reversed, email: "24f2001614@ds.study.iitm.ac.in" });
});
app.listen(3000);
