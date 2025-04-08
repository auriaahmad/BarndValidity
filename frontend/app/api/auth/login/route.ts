import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { email, password } = body;

    // In a real application, you would validate the credentials against your backend
    // For this example, we'll use a mock response
    if (email === 'admin@example.com' && password === 'admin123') {
      return NextResponse.json({
        access_token: 'mock-jwt-token',
        token_type: 'bearer',
      });
    }

    return NextResponse.json(
      { error: 'Invalid credentials' },
      { status: 401 }
    );
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
} 