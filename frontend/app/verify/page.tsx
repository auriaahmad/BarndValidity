'use client';

import { useState } from 'react';

export default function VerifyPage() {
  const [qrCode, setQrCode] = useState('');
  const [verificationResult, setVerificationResult] = useState<null | { valid: boolean; message: string }>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // Handle QR code verification
    // This is a mock implementation
    setVerificationResult({
      valid: true,
      message: 'Product is authentic',
    });
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto">
        <div className="text-center">
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Verify Product
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            Enter the QR code to verify your product's authenticity
          </p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="qrCode" className="sr-only">
              QR Code
            </label>
            <input
              id="qrCode"
              name="qrCode"
              type="text"
              required
              className="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Enter QR Code"
              value={qrCode}
              onChange={(e) => setQrCode(e.target.value)}
            />
          </div>

          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Verify
            </button>
          </div>
        </form>

        {verificationResult && (
          <div className={`mt-4 p-4 rounded-md ${verificationResult.valid ? 'bg-green-50' : 'bg-red-50'}`}>
            <p className={`text-sm ${verificationResult.valid ? 'text-green-700' : 'text-red-700'}`}>
              {verificationResult.message}
            </p>
          </div>
        )}
      </div>
    </div>
  );
} 