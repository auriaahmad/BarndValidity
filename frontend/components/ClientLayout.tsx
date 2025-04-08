'use client';

import { usePathname } from 'next/navigation';
import Navbar from './Navbar';
import Footer from './Footer';

interface ClientLayoutProps {
  children: React.ReactNode;
}

export default function ClientLayout({ children }: ClientLayoutProps) {
  const pathname = usePathname();

  // Define routes where header and footer should be hidden
  const excludedRoutes = [
    '/admin/login',
    '/admin/dashboard',
    '/admin/batches',
    '/admin/products',
    // Add more admin routes as needed
  ];

  const shouldShowHeaderFooter = !excludedRoutes.some(route => pathname?.startsWith(route));

  return (
    <div className="flex flex-col min-h-screen">
      {shouldShowHeaderFooter && <Navbar />}
      <main className={`flex-grow ${shouldShowHeaderFooter ? 'pt-16' : ''}`}>
        {children}
      </main>
      {shouldShowHeaderFooter && <Footer />}
    </div>
  );
} 