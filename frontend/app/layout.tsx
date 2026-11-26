import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Django ToDo Training!",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ja">
      <body>
        <div className="djangotrainingAppWrapper">{children}</div>
      </body>
    </html>
  );
}
