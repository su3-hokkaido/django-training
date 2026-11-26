import type { NextConfig } from "next";

const djangoUrl = process.env.DJANGO_URL ?? "http://127.0.0.1:8000";

const nextConfig: NextConfig = {
  // Django の URL は末尾が / なので合わせる
  trailingSlash: true,
  // /api/... へのリクエストは Django に中継する (ブラウザからは同じオリジンに見える)
  async rewrites() {
    return [{ source: "/api/:path*/", destination: `${djangoUrl}/api/:path*/` }];
  },
};

export default nextConfig;
