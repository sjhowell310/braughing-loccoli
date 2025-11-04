import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

interface HealthResponse {
  status: string;
}

export default function Home() {
  const [health, setHealth] = useState<string>("checking...");

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((res) => res.json())
      .then((data: HealthResponse) => setHealth(data.status))
      .catch(() => setHealth("unreachable"));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-indigo-50 to-white text-gray-800">
      <h1 className="text-5xl font-bold mb-4">🚀 Braughing Loccoli</h1>
      <p className="text-lg text-gray-600 mb-6">
        Welcome to your full-stack playground.
      </p>

      <section className="border border-gray-200 rounded-xl px-6 py-4 shadow-sm bg-white">
        <h2 className="text-xl font-semibold mb-2">Backend Health</h2>
        <p>
          FastAPI status:{" "}
          <span
            className={`font-semibold ${
              health === "ok"
                ? "text-green-600"
                : health === "unreachable"
                ? "text-red-600"
                : "text-yellow-600"
            }`}
          >
            {health}
          </span>
        </p>
      </section>

      <footer className="mt-12 text-sm text-gray-400">
        Powered by FastAPI ⚡ + React ⚛️ + Vite ⚙️
      </footer>
    </main>
  );
}
