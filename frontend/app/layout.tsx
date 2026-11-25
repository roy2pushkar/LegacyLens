import type { Metadata } from 'next';
import '@xyflow/react/dist/style.css';
import './globals.css';
export const metadata: Metadata = { title: 'LegacyLens | Mainframe Intelligence', description: 'Understand legacy mainframe applications with code and dependency analysis.' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
