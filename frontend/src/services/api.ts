// src/client/api.ts

import { OpenAPI, ApiError } from './core';

const api = {
  get: async <T>(url: string, params?: Record<string, string>) => {
    try {
      const queryString = params ? `?${new URLSearchParams(params).toString()}` : '';
      const response = await fetch(`${OpenAPI.BASE}/api${url}${queryString}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...(OpenAPI.TOKEN && { Authorization: `Bearer ${OpenAPI.TOKEN}` }),
        },
      });
      if (!response.ok) throw new ApiError(response, 'An error occurred while fetching the data.');
      return await response.json() as T;
    } catch (error) {
      console.error('API Get Error:', error);
      throw error;
    }
  },

  patch: async <T>(url: string, data: any) => {
    try {
      const response = await fetch(`${OpenAPI.BASE}/api${url}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          ...(OpenAPI.TOKEN && { Authorization: `Bearer ${OpenAPI.TOKEN}` }),
        },
        body: JSON.stringify(data),
      });
      if (!response.ok) throw new ApiError(response, 'An error occurred while updating the data.');
      return await response.json() as T;
    } catch (error) {
      console.error('API Patch Error:', error);
      throw error;
    }
  },
};

export default api;