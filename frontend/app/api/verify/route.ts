import { NextResponse } from 'next/server';
import { headers } from 'next/headers';

// Mock data for demonstration
const mockProducts = [
  {
    unique_code: 'BATCH001_1',
    batch_id: 1,
    is_verified: false,
    verification_date: null,
  },
  {
    unique_code: 'BATCH001_2',
    batch_id: 1,
    is_verified: true,
    verification_date: '2024-01-01T12:00:00Z',
  },
];

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const code = searchParams.get('code');

    if (!code) {
      return NextResponse.json(
        {
          status: 'Invalid',
          message: 'No verification code provided',
        },
        { status: 400 }
      );
    }

    const product = mockProducts.find((p) => p.unique_code === code);

    if (!product) {
      return NextResponse.json({
        status: 'Invalid',
        message: 'Product not found or invalid code',
      });
    }

    if (product.is_verified) {
      return NextResponse.json({
        status: 'Already Verified',
        product_info: product,
        message: 'This product has already been verified',
      });
    }

    // In a real application, you would update the verification status in your backend
    // For this example, we'll return a mock response
    return NextResponse.json({
      status: 'Authentic',
      product_info: {
        ...product,
        is_verified: true,
        verification_date: new Date().toISOString(),
      },
      message: 'Product successfully verified',
    });
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
} 