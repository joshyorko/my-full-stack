// routes/management-dashboard.tsx

import { createFileRoute } from '@tanstack/react-router';
import ManagementDashboard from '../components/Allocation/ManagementDashboard'; 
import useAuth from '../hooks/useAuth';

export const Route = createFileRoute('/management-dashboard')({
  component: ManagementDashboard,
  // You can add optional route hooks like `beforeLoad` if needed
});

export default ManagementDashboard;

