import { Sidebar } from '@/components/layout/Sidebar';
import { VideoCanvas } from '@/components/editor/VideoCanvas';
import { ClipSidebar } from '@/components/editor/ClipSidebar';
import { Settings, Share2, ArrowLeft } from 'lucide-react';
import Link from 'next/link';

export default function EditorPage({ params }: { params: { id: string } }) {
  return (
    <main className="flex h-screen bg-black text-slate-100 overflow-hidden">
      {/* Mini Nav */}
      <nav className="fixed top-0 inset-x-0 h-14 border-b border-slate-800 bg-slate-950/50 backdrop-blur-xl flex items-center justify-between px-6 z-50">
        <div className="flex items-center gap-4">
          <Link href="/dashboard" className="p-2 hover:bg-slate-800 rounded-lg text-slate-400">
            <ArrowLeft size={20} />
          </Link>
          <h1 className="font-bold text-sm tracking-widest uppercase">
            Editing: <span className="text-indigo-400">SaaS_Growth_Masterclass.mp4</span>
          </h1>
        </div>
        
        <div className="flex items-center gap-3">
          <button className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 rounded-lg text-sm hover:bg-slate-700 transition-colors">
            <Settings size={16} />
            Config
          </button>
          <button className="flex items-center gap-2 px-4 py-1.5 bg-indigo-600 rounded-lg text-sm font-bold hover:bg-indigo-500 transition-colors">
            <Share2 size={16} />
            Publish
          </button>
        </div>
      </nav>

      <div className="flex flex-1 pt-14">
        {/* Main Workspace */}
        <VideoCanvas videoUrl="" />
        
        {/* Right Sidebar - AI Clips */}
        <ClipSidebar />
      </div>
    </main>
  );
}