import React from 'react';
import { Play, BarChart3, Clock, ChevronRight } from 'lucide-react';
import { VideoProject } from '@/types/video';

export const VideoCard = ({ project }: { project: VideoProject }) => {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden hover:border-indigo-500/50 transition-all group">
      <div className="aspect-video bg-slate-800 relative">
        <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 to-transparent" />
        <div className="absolute bottom-3 left-3 flex items-center gap-2">
          <span className="px-2 py-1 bg-indigo-600 text-[10px] font-bold uppercase rounded">AI Processed</span>
        </div>
      </div>
      
      <div className="p-4">
        <h3 className="text-white font-medium truncate mb-2">{project.originalTitle}</h3>
        
        <div className="flex items-center justify-between text-slate-400 text-sm mb-4">
          <div className="flex items-center gap-1">
            <Clock size={14} />
            <span>{Math.floor(project.duration / 60)}m</span>
          </div>
          <div className="flex items-center gap-1">
            <BarChart3 size={14} className="text-emerald-400" />
            <span className="text-emerald-400 font-semibold">{project.clips.length} Clips Found</span>
          </div>
        </div>

        <button className="w-full py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg flex items-center justify-center gap-2 transition-colors">
          Open Editor
          <ChevronRight size={16} />
        </button>
      </div>
    </div>
  );
};