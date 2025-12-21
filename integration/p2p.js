const Libp2p = require('libp2p');
const TCP = require('libp2p-tcp');
const { NOISE } = require('libp2p-noise');
const MPLEX = require('libp2p-mplex');

async function startP2PNode() {
  const libp2p = await Libp2p.create({
    addresses: { listen: ['/ip4/0.0.0.0/tcp/0'] },
    modules: {
      transport: [TCP],
      connEncryption: [NOISE],
      streamMuxer: [MPLEX]
    }
  });
  await libp2p.start();
  console.log('P2P node started on port', libp2p.multiaddrs[0].toString());
  return libp2p;
}

module.exports = { startP2PNode };
