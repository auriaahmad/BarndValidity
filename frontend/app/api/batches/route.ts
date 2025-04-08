import { NextResponse } from 'next/server';
import { headers } from 'next/headers';

// Mock data for demonstration
const mockBatches = [
  {
    id: 1,
    school_name: 'Example School',
    product_type: 'shirt',
    batch_number: 'BATCH001',
    quantity: 100,
    created_at: '2024-01-01T00:00:00Z',
  },
  {
    id: 2,
    school_name: 'Another School',
    product_type: 'pants',
    batch_number: 'BATCH002',
    quantity: 50,
    created_at: '2024-01-02T00:00:00Z',
  },
];

export async function GET() {
  try {
    const headersList = headers();
    const token = headersList.get('authorization')?.split(' ')[1];

    if (!token) {
      return NextResponse.json(
        { error: 'Unauthorized' },
        { status: 401 }
      );
    }

    return NextResponse.json(mockBatches);
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const headersList = headers();
    const token = headersList.get('authorization')?.split(' ')[1];

    if (!token) {
      return NextResponse.json(
        { error: 'Unauthorized' },
        { status: 401 }
      );
    }

    const body = await request.json();
    const { school_name, product_type, batch_number, quantity } = body;

    // In a real application, you would create the batch in your backend
    // For this example, we'll return a mock response
    const newBatch = {
      id: mockBatches.length + 1,
      school_name,
      product_type,
      batch_number,
      quantity,
      created_at: new Date().toISOString(),
    };

    return NextResponse.json(newBatch, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
} 