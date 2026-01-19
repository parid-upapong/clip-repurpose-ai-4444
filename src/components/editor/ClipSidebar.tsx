import React from 'react';
import { CheckCircle2, Flame, Scissors } from 'lucide-react';

const MOCK_CLIPS = [
  { id: '1', score: 98, time: '00:12 - 00:45', hook: 'The secret to scaling SaaS' },
  { id: '2', score: 85, time: '01:05 - 01:30', hook: 'Why AI won\'t replace you' },
  { id: '3', score: 72, time: '04:20 - 05:00', hook: 'Investment strategies for 2024' },
];

export const ClipSidebar = () => {
  return (
    <div className="w-80 border-l border-slate-800 bg-slate-950 flex flex-col">
      <div className="p-4 border-b border-slate-800">
        <h2 className="text-white font-bold flex items-center gap-2">
          <Flame size={18} className="text-orange-500" />
          AI Highlights
        </h2>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {MOCK_CLIPS.map((clip) => (
          <div key={clip.id} className="p-3 bg-slate-900 rounded-xl border border-slate-800 hover:border-indigo-500 cursor-pointer group transition-all">
            <div className="flex justify-between items-start mb-2">
              <span className="text-[10px] font-bold px-2 py-0.5 bg-indigo-500/10 text-indigo-400 rounded-full border border-indigo-500/20">
                SCORE: {clip.score}
              </span>
              <Scissors size={14} className="text-slate-600 group-hover:text-white" />
            </div>
            <p className="text-sm text-slate-200 font-medium mb-2 leading-snug">
              {clip.hook}
            </p>
            <div className="flex items-center justify-between text-[11px] text-slate-500">
              <span>{clip.time}</span>
              <CheckCircle2 size={14} className="text-emerald-500" />
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 bg-slate-900 border-t border-slate-800">
        <button className="w-full py-3 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl shadow-lg shadow-indigo-500/20 transition-all">
          Export All Clips
        </button>
      </div>
    </div>
  );
};