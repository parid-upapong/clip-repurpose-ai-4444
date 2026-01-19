import React from 'react';

const LandingPage = () => {
  return (
    <div className="bg-slate-900 text-white min-h-screen font-sans">
      <nav className="p-6 flex justify-between items-center border-b border-slate-800">
        <h1 className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
          OVERLORD AI
        </h1>
        <button className="bg-blue-600 px-6 py-2 rounded-full font-semibold hover:bg-blue-500 transition">
          Launch App
        </button>
      </nav>

      <main className="max-w-6xl mx-auto mt-20 text-center px-4">
        <h2 className="text-6xl font-extrabold mb-6 leading-tight">
          Turn Your Long Videos into <br/> 
          <span className="text-cyan-400 font-mono italic">Viral Gold</span>
        </h2>
        <p className="text-xl text-slate-400 mb-10 max-w-2xl mx-auto">
          The ultimate AI platform for creators. Extract high-impact clips for TikTok, Reels, and Shorts automatically. Save hours of editing.
        </p>

        <div className="flex gap-4 justify-center">
          <button className="bg-white text-slate-900 px-8 py-4 rounded-lg text-lg font-bold">
            Start Free Trial
          </button>
          <button className="border border-slate-700 px-8 py-4 rounded-lg text-lg font-bold hover:bg-slate-800">
            Watch Demo
          </button>
        </div>

        <div className="mt-20 border border-slate-800 rounded-2xl bg-slate-950 p-2 shadow-2xl">
          <div className="bg-slate-900 rounded-xl p-12 flex flex-col items-center border border-slate-800">
             <div className="w-20 h-20 bg-blue-500/20 rounded-full flex items-center justify-center mb-4">
                <div className="w-10 h-10 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
             </div>
             <p className="text-slate-300 font-medium">AI is scanning your footage for viral moments...</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default LandingPage;