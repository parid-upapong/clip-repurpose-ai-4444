'use client';
import React, { useState } from 'react';
import { Maximize, Smartphone, User, RefreshCcw } from 'lucide-react';

export const VideoCanvas = ({ videoUrl }: { videoUrl: string }) => {
  const [activeSpeakerMode, setActiveSpeakerMode] = useState(true);

  return (
    <div className="flex-1 bg-black flex flex-col items-center justify-center p-8 relative">
      {/* 9:16 Framing Container */}
      <div className="relative aspect-[9/16] h-full max-h-[700px] bg-slate-900 rounded-2xl shadow-2xl border-4 border-slate-800 overflow-hidden">
        {/* Mock Video Stream */}
        <div className="absolute inset-0 flex items-center justify-center">
            <img 
                src="https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=1000&auto=format&fit=crop" 
                className="h-full w-auto max-w-none scale-150 grayscale-[0.2]"
                alt="Speaker focus"
            />
            
            {/* AI Speaker Tracking Overlay (Face Bounding Box) */}
            {activeSpeakerMode && (
                <div className="absolute top-1/4 w-32 h-32 border-2 border-emerald-400 rounded-lg animate-pulse">
                    <div className="absolute -top-6 left-0 bg-emerald-400 text-[10px] text-black font-bold px-1 rounded">
                        SPEAKER_01
                    </div>
                </div>
            )}
        </div>

        {/* Caption Overlay Preview */}
        <div className="absolute bottom-20 inset-x-0 px-6 text-center">
          <h2 className="text-white text-2xl font-black italic uppercase leading-tight drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)]">
            "This is how we build <span className="text-yellow-400">Viral AI</span> content!"
          </h2>
        </div>
      </div>

      {/* Editor Controls Overlay */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-4 bg-slate-900/90 backdrop-blur-md p-2 rounded-2xl border border-slate-700">
        <button 
            onClick={() => setActiveSpeakerMode(!activeSpeakerMode)}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl transition-all ${activeSpeakerMode ? 'bg-indigo-600 text-white' : 'text-slate-400'}`}
        >
          <User size={18} />
          <span className="text-sm font-medium">Auto-Speaker</span>
        </button>
        <div className="w-px h-6 bg-slate-700" />
        <button className="p-2 text-slate-400 hover:text-white">
          <RefreshCcw size={18} />
        </button>
        <button className="p-2 text-slate-400 hover:text-white">
          <Smartphone size={18} />
        </button>
      </div>
    </div>
  );
};