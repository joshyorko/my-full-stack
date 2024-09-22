/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

// Import Routes

import { Route as rootRoute } from './routes/__root'
console.log('rootRoute imported:', rootRoute);

import { Route as SignupImport } from './routes/signup'
console.log('SignupImport imported:', SignupImport);

import { Route as ResetPasswordImport } from './routes/reset-password'
console.log('ResetPasswordImport imported:', ResetPasswordImport);

import { Route as RecoverPasswordImport } from './routes/recover-password'
console.log('RecoverPasswordImport imported:', RecoverPasswordImport);



import { Route as LoginImport } from './routes/login'
console.log('LoginImport imported:', LoginImport);

import { Route as AdjudicatorDashboardImport } from './routes/adjudicator-dashboard'
console.log('AdjudicatorDashboardImport imported:', AdjudicatorDashboardImport);

import { Route as LayoutImport } from './routes/_layout'
console.log('LayoutImport imported:', LayoutImport);

import { Route as LayoutIndexImport } from './routes/_layout/index'
console.log('LayoutIndexImport imported:', LayoutIndexImport);

import { Route as LayoutSettingsImport } from './routes/_layout/settings'
console.log('LayoutSettingsImport imported:', LayoutSettingsImport);

import { Route as LayoutItemsImport } from './routes/_layout/items'
console.log('LayoutItemsImport imported:', LayoutItemsImport);

import { Route as LayoutAdminImport } from './routes/_layout/admin'
console.log('LayoutAdminImport imported:', LayoutAdminImport);

// Create/Update Routes

const SignupRoute = SignupImport.update({
  path: '/signup',
  getParentRoute: () => rootRoute,
} as any)
console.log('SignupRoute created:', SignupRoute);

const ResetPasswordRoute = ResetPasswordImport.update({
  path: '/reset-password',
  getParentRoute: () => rootRoute,
} as any)
console.log('ResetPasswordRoute created:', ResetPasswordRoute);

const RecoverPasswordRoute = RecoverPasswordImport.update({
  path: '/recover-password',
  getParentRoute: () => rootRoute,
} as any)
console.log('RecoverPasswordRoute created:', RecoverPasswordRoute);



const LoginRoute = LoginImport.update({
  path: '/login',
  getParentRoute: () => rootRoute,
} as any)
console.log('LoginRoute created:', LoginRoute);

const AdjudicatorDashboardRoute = {
  path: '/adjudicator-dashboard',
  component: AdjudicatorDashboardImport.component, // Properly referenced component
  getParentRoute: () => rootRoute,
};
console.log('AdjudicatorDashboardRoute created:', AdjudicatorDashboardRoute);

const LayoutRoute = LayoutImport.update({
  id: '/_layout',
  getParentRoute: () => rootRoute,
} as any)
console.log('LayoutRoute created:', LayoutRoute);

const LayoutIndexRoute = LayoutIndexImport.update({
  path: '/',
  getParentRoute: () => LayoutRoute,
} as any)
console.log('LayoutIndexRoute created:', LayoutIndexRoute);

const LayoutSettingsRoute = LayoutSettingsImport.update({
  path: '/settings',
  getParentRoute: () => LayoutRoute,
} as any)
console.log('LayoutSettingsRoute created:', LayoutSettingsRoute);

const LayoutItemsRoute = LayoutItemsImport.update({
  path: '/items',
  getParentRoute: () => LayoutRoute,
} as any)
console.log('LayoutItemsRoute created:', LayoutItemsRoute);

const LayoutAdminRoute = LayoutAdminImport.update({
  path: '/admin',
  getParentRoute: () => LayoutRoute,
} as any)
console.log('LayoutAdminRoute created:', LayoutAdminRoute);

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/_layout': {
      preLoaderRoute: typeof LayoutImport
      parentRoute: typeof rootRoute
    }
    '/adjudicator-dashboard': {
      preLoaderRoute: typeof AdjudicatorDashboardImport
      parentRoute: typeof rootRoute
    }
    '/login': {
      preLoaderRoute: typeof LoginImport
      parentRoute: typeof rootRoute
    }

    '/recover-password': {
      preLoaderRoute: typeof RecoverPasswordImport
      parentRoute: typeof rootRoute
    }
    '/reset-password': {
      preLoaderRoute: typeof ResetPasswordImport
      parentRoute: typeof rootRoute
    }
    '/signup': {
      preLoaderRoute: typeof SignupImport
      parentRoute: typeof rootRoute
    }
    '/_layout/admin': {
      preLoaderRoute: typeof LayoutAdminImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/items': {
      preLoaderRoute: typeof LayoutItemsImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/settings': {
      preLoaderRoute: typeof LayoutSettingsImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/': {
      preLoaderRoute: typeof LayoutIndexImport
      parentRoute: typeof LayoutImport
    }
  }
}

// Create and export the route tree

export const routeTree = rootRoute.addChildren([
  LayoutRoute.addChildren([
    LayoutAdminRoute,
    LayoutItemsRoute,
    LayoutSettingsRoute,
    LayoutIndexRoute,
  ]),
  AdjudicatorDashboardRoute,
  LoginRoute,
  RecoverPasswordRoute,
  ResetPasswordRoute,
  SignupRoute,
])
console.log('routeTree created:', routeTree);

/* prettier-ignore-end */
