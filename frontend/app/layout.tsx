import type { Metadata } from "next";
import "./globals.css";
import { inter } from '@/app/ui/fonts';
import { AppRouterCacheProvider } from "@mui/material-nextjs/v13-appRouter";
import ErrorDialog from "@/app/ui/commons/error_dialog";

export const metadata: Metadata = {
  title: "vital viewer",
  description: "wearable device data viewer",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <AppRouterCacheProvider>
        <body className={`${inter.className} antialiased`}>{children}</body>
        <ErrorDialog />
      </AppRouterCacheProvider>
    </html>
  );
}
