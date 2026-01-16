module.exports = {
  reactStrictMode: true,
  output: 'export',

  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/:path*',
      },
    ];
  },
};
