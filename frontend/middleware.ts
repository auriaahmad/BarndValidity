import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;
  
  // Check if the route is an admin route
  if (pathname.startsWith('/admin')) {
    // For non-login admin routes, check authentication
    if (pathname !== '/admin/login') {
      const token = request.cookies.get('auth-token');
      if (!token) {
        return NextResponse.redirect(new URL('/admin/login', request.url));
      }
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/admin/:path*',
}; 