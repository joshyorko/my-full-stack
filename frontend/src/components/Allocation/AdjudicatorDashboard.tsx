import React, { useState, useEffect } from 'react';
import { Clock } from 'lucide-react';
import { useAuth } from '../../hooks/useAuth'; // Adjust this import based on your actual auth hook

interface Claim {
  dcn: string;
  electronic_attachments: string;
  [key: string]: any;
}

interface WorkCounts {
  queue: number;
  completed: number;
  skipped: number;
}

const ClaimTable: React.FC<{ claim: Claim }> = ({ claim }) => (
  <div className="w-1/2 p-4 overflow-auto">
    <table className="w-full border-collapse">
      <tbody>
        {Object.entries(claim).map(([key, value]) => (
          <tr key={key} className="border-b">
            <td className="p-2 font-semibold">{key}</td>
            <td className="p-2">{String(value)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

const ImageViewer: React.FC<{ attachmentId: string }> = ({ attachmentId }) => (
  <div className="w-1/2 p-4">
    <div className="bg-gray-200 h-full flex items-center justify-center">
      <p>Image Viewer (Attachment ID: {attachmentId})</p>
    </div>
  </div>
);

const StatusBar: React.FC<WorkCounts & { avgTransactionTime: number }> = ({ 
  queue, completed, skipped, avgTransactionTime 
}) => (
  <div className="bg-blue-100 p-4 mb-4 flex justify-between items-center">
    <div>Queue: {queue}</div>
    <div>Completed: {completed}</div>
    <div>Skipped: {skipped}</div>
    <div>Avg Time: {avgTransactionTime.toFixed(2)}s</div>
  </div>
);

export default function AdjudicatorDashboard() {
  const [currentClaim, setCurrentClaim] = useState<Claim | null>(null);
  const [workCounts, setWorkCounts] = useState<WorkCounts>({ queue: 0, completed: 0, skipped: 0 });
  const [startTime, setStartTime] = useState<Date | null>(null);
  const { user } = useAuth(); // Use your actual auth hook

  useEffect(() => {
    if (user) {
      fetchNextClaim();
      fetchWorkCounts();
    }
  }, [user]);

  const fetchNextClaim = async () => {
    try {
      const response = await fetch('/api/allocation/get_work');
      const data = await response.json();
      setCurrentClaim(data);
      setStartTime(new Date());
    } catch (error) {
      console.error('Error fetching next claim:', error);
    }
  };

  const fetchWorkCounts = async () => {
    try {
      const response = await fetch('/api/allocation/get_work_count');
      const data = await response.json();
      setWorkCounts(data);
    } catch (error) {
      console.error('Error fetching work counts:', error);
    }
  };

  const handleAction = async (action: 'Skipped' | 'Completed') => {
    if (!currentClaim || !startTime) return;

    const stopTime = new Date();
    const duration = (stopTime.getTime() - startTime.getTime()) / 1000;

    try {
      await fetch('/api/allocation/update_status', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dcn: currentClaim.dcn, status: action, duration })
      });
      await fetchNextClaim();
      await fetchWorkCounts();
    } catch (error) {
      console.error(`Error ${action.toLowerCase()} claim:`, error);
    }
  };

  if (!user) return <div>Please log in to access the Adjudicator Dashboard</div>;
  if (!currentClaim) return <div>Loading...</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Adjudicator Dashboard</h1>
      <StatusBar {...workCounts} avgTransactionTime={avgTransactionTime} />
      <div className="flex mb-4">
        <ClaimTable claim={currentClaim} />
        <ImageViewer attachmentId={currentClaim.electronic_attachments} />
      </div>
      <div className="flex justify-between items-center">
        <div className="flex items-center">
          <Clock className="mr-2" />
          Start Time: {startTime?.toLocaleTimeString()}
        </div>
        <div>
          <button 
            onClick={() => handleAction('Skipped')} 
            className="bg-yellow-500 text-white px-4 py-2 rounded mr-2"
          >
            Skip
          </button>
          <button 
            onClick={() => handleAction('Completed')} 
            className="bg-green-500 text-white px-4 py-2 rounded"
          >
            Complete
          </button>
        </div>
      </div>
    </div>
  );
}