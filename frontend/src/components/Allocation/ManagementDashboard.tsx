import React, { useState, useEffect } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import useAuth from '../../hooks/useAuth'; // Adjust this import based on your actual auth hook

interface AdjudicatorData {
  name: string;
  claimsProcessed: number;
  avgTime: number;
}

interface OverallStats {
  totalClaims: number;
  avgTime: number;
  inQueue: number;
  activeAdjudicators: number;
}

const AdjudicatorPerformance: React.FC<{ data: AdjudicatorData[] }> = ({ data }) => (
  <div className="bg-white p-4 rounded-lg shadow">
    <h2 className="text-xl font-bold mb-4">Adjudicator Performance</h2>
    {data.length > 0 ? (
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis yAxisId="left" orientation="left" stroke="#8884d8" />
          <YAxis yAxisId="right" orientation="right" stroke="#82ca9d" />
          <Tooltip />
          <Legend />
          <Bar yAxisId="left" dataKey="claimsProcessed" fill="#8884d8" name="Claims Processed" />
          <Bar yAxisId="right" dataKey="avgTime" fill="#82ca9d" name="Avg Time (s)" />
        </BarChart>
      </ResponsiveContainer>
    ) : (
      <p>No data available for Adjudicator Performance</p>
    )}
  </div>
);

const OverallStatsComponent: React.FC<{ stats: OverallStats }> = ({ stats }) => (
  <div className="bg-white p-4 rounded-lg shadow">
    <h2 className="text-xl font-bold mb-4">Overall Statistics</h2>
    <div className="grid grid-cols-2 gap-4">
      <div>
        <p className="text-lg font-semibold">Total Claims Processed</p>
        <p className="text-3xl font-bold text-blue-600">{stats.totalClaims}</p>
      </div>
      <div>
        <p className="text-lg font-semibold">Average Processing Time</p>
        <p className="text-3xl font-bold text-green-600">{stats.avgTime.toFixed(2)}s</p>
      </div>
      <div>
        <p className="text-lg font-semibold">Claims in Queue</p>
        <p className="text-3xl font-bold text-yellow-600">{stats.inQueue}</p>
      </div>
      <div>
        <p className="text-lg font-semibold">Active Adjudicators</p>
        <p className="text-3xl font-bold text-purple-600">{stats.activeAdjudicators}</p>
      </div>
    </div>
  </div>
);

export default function ManagementDashboard() {
  const [adjudicatorData, setAdjudicatorData] = useState<AdjudicatorData[]>([]);
  const [overallStats, setOverallStats] = useState<OverallStats>({
    totalClaims: 0,
    avgTime: 0,
    inQueue: 0,
    activeAdjudicators: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { user } = useAuth(); // Use your actual auth hook

  useEffect(() => {
    if (user) {
      fetchData();
    }
  }, [user]);

  const fetchData = async () => {
    setLoading(true);
    setError(null); // Reset error state
    try {
      const response = await fetch('/api/allocation/management_stats');
      if (!response.ok) {
        throw new Error('Error fetching management stats');
      }
      const data = await response.json();
      setAdjudicatorData(data.adjudicatorData ?? []);
      setOverallStats(data.overallStats ?? {
        totalClaims: 0,
        avgTime: 0,
        inQueue: 0,
        activeAdjudicators: 0,
      });
    } catch (error) {
      setError((error as Error).message);
    } finally {
      setLoading(false);
    }
  };

  if (!user) return <div>Please log in to access the Management Dashboard</div>;

  if (loading) return <div>Loading data...</div>;

  if (error) return <div>Error: {error}</div>;

  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Management Live Reporting Dashboard</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <AdjudicatorPerformance data={adjudicatorData} />
        <OverallStatsComponent stats={overallStats} />
      </div>
    </div>
  );
}
