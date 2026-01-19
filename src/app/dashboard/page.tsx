import { VideoCard } from '@/components/dashboard/VideoCard';
import { Plus, LayoutGrid, List, Search } from 'lucide-react';

const MOCK_PROJECTS = [
  {
    id: 'proj_1',
    originalTitle: 'The Future of AI Hardware with Jensen Huang',
    duration: 3600,
    clips: [{}, {}, {}, {}],
    createdAt: '2023-11-20',
  },
  {
    id: 'proj_2',
    originalTitle: 'Modern Architecture Patterns in 2024',
    duration: 1800,
    clips: [{}, {}, {}],
    createdAt: '2023-11-21',
  }
];

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8">
      <header className="max-w-7xl mx-auto flex justify-between items-end mb-12">
        <div>
          <h1 className="text-4xl font-black mb-2 tracking-tight">Your Content Library</h1>
          <p className="text-slate-400">Transform your long-form videos into viral goldmines.</p>
        </div>
        <button className="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-3 rounded-xl font-bold flex items-center gap-2 transition-all shadow-lg shadow-indigo-600/20">
          <Plus size={20} />
          Upload New Video
        </button>
      </header>

      <div className="max-w-7xl mx-auto">
        <div className="flex items-center justify-between mb-8 pb-4 border-b border-slate-900">
          <div className="flex gap-4">
            <button className="text-white border-b-2 border-indigo-500 pb-4 px-2 font-medium">All Projects</button>
            <button className="text-slate-500 hover:text-slate-300 pb-4 px-2 font-medium">Processing</button>
            <button className="text-slate-500 hover:text-slate-300 pb-4 px-2 font-medium">Scheduled</button>
          </div>
          <div className="flex items-center gap-2 bg-slate-900 rounded-lg px-3 py-1.5 border border-slate-800">
            <Search size={16} className="text-slate-500" />
            <input 
              type="text" 
              placeholder="Search videos..." 
              className="bg-transparent border-none outline-none text-sm w-48"
            />
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {MOCK_PROJECTS.map((project) => (
            <VideoCard key={project.id} project={project as any} />
          ))}
        </div>
      </div>
    </div>
  );
}