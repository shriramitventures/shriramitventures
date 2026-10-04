import os

services_data = [
    {
        "category": "1. 🤖 Artificial Intelligence, Machine Learning & Agentic Systems",
        "anchor": "1--artificial-intelligence-machine-learning--agentic-systems",
        "intro": "We engineer production-grade Generative AI, autonomous multi-agent workflows, enterprise RAG architectures, and custom Model Context Protocol (MCP) servers. Our AI deployments are built with evaluation harnesses, human-in-the-loop review gates, and drift monitoring in CI/CD pipelines so models stay accurate and cost-effective after initial release.",
        "services": [
            {
                "slug": "ai-ml-solutions",
                "name": "AI / ML Solutions",
                "url": "https://www.shriramitventures.com/ai-ml-solutions",
                "desc": "End-to-end artificial intelligence and machine learning engineering. We design custom predictive models, recommendation algorithms, computer vision pipelines, and intelligent decision systems integrated natively into core SaaS and enterprise workflows.",
                "keywords": "AI ML engineering, predictive analytics, enterprise machine learning, custom AI models, production AI integration"
            },
            {
                "slug": "generative-ai-development",
                "name": "Generative AI Development",
                "url": "https://www.shriramitventures.com/generative-ai-development",
                "desc": "Custom Generative AI applications leveraging frontier foundation models. From fine-tuned text synthesis and domain-specific code assistants to automated multimodal content pipelines powered by OpenAI, Claude, and Gemini.",
                "keywords": "Generative AI consulting, GenAI applications, enterprise generative AI, custom foundation model fine-tuning"
            },
            {
                "slug": "llm-development",
                "name": "Large Language Model (LLM) Development",
                "url": "https://www.shriramitventures.com/llm-development",
                "desc": "Domain-specific LLM fine-tuning (LoRA/QLoRA), model quantization, semantic caching, prompt engineering, and cost-optimized token routing. We turn open-source and proprietary models into defensible enterprise IP.",
                "keywords": "LLM fine-tuning, large language models, enterprise LLM development, prompt engineering, token cost reduction"
            },
            {
                "slug": "ai-agent-development",
                "name": "Autonomous AI Agent Development",
                "url": "https://www.shriramitventures.com/ai-agent-development",
                "desc": "Autonomous multi-agent systems engineered with LangGraph, AutoGen, and CrewAI. We build self-correcting agents capable of multi-step planning, tool-calling, external API interaction, and automated operational execution with human oversight.",
                "keywords": "AI agent development, autonomous agents, LangGraph agents, multi-agent workflows, tool-calling AI"
            },
            {
                "slug": "rag-systems",
                "name": "Retrieval-Augmented Generation (RAG) Systems",
                "url": "https://www.shriramitventures.com/rag-systems",
                "desc": "Enterprise RAG architectures linking enterprise knowledge repositories with LLMs. Features hybrid BM25 and dense vector search, semantic chunking, cross-encoder reranking, and sub-second retrieval latency.",
                "keywords": "RAG systems, retrieval-augmented generation, enterprise search, vector search, hybrid retrieval"
            },
            {
                "slug": "rag-development",
                "name": "Enterprise RAG Pipeline Development",
                "url": "https://www.shriramitventures.com/rag-development",
                "desc": "End-to-end RAG data pipelines featuring real-time document ingestion, automated OCR parsing, hallucination guards (Ragas/TruLens evaluation), strict role-based access control, and verifiable source citations.",
                "keywords": "RAG pipeline development, document ingestion pipeline, enterprise vector databases, hallucination guardrails"
            },
            {
                "slug": "ai-chatbot-development",
                "name": "AI Chatbot Development",
                "url": "https://www.shriramitventures.com/ai-chatbot-development",
                "desc": "Intelligent conversational agents supporting multi-turn dialogue, context memory, CRM lead qualification, and sentiment analysis. Fully integrated with WhatsApp, web chat, Slack, and Zendesk.",
                "keywords": "AI chatbot development, conversational AI, smart customer support bot, WhatsApp AI bot"
            },
            {
                "slug": "mcp-server-development",
                "name": "Model Context Protocol (MCP) Server Development",
                "url": "https://www.shriramitventures.com/mcp-server-development",
                "desc": "Architecting bespoke MCP servers adhering to Anthropic's open standard. Connect AI models securely to local datasets, proprietary databases, enterprise ERPs, and cloud developer tools without API credential leaks.",
                "keywords": "MCP server development, Model Context Protocol, Claude MCP server, custom MCP tools, AI context protocol"
            },
            {
                "slug": "mcp-development",
                "name": "Custom MCP Tooling & Client Integration",
                "url": "https://www.shriramitventures.com/mcp-development",
                "desc": "Bespoke Model Context Protocol integrations empowering internal development teams and AI agents to query databases, run bash scripts, and interact with production microservices within strict sandboxed guardrails.",
                "keywords": "MCP development, custom MCP tooling, agentic MCP integration, Model Context Protocol clients"
            },
            {
                "slug": "voice-ai-assistants",
                "name": "Voice AI Assistants",
                "url": "https://www.shriramitventures.com/voice-ai-assistants",
                "desc": "Low-latency conversational voice bots powered by WebRTC, Whisper speech-to-text, and ElevenLabs/Cartesia synthesis. Delivers sub-600ms latency for human-like phone customer service and appointment booking.",
                "keywords": "Voice AI assistants, conversational voice bot, real-time voice AI, AI call center, automated phone receptionist"
            },
            {
                "slug": "voice-ai-development",
                "name": "Real-Time Voice AI Agent Development",
                "url": "https://www.shriramitventures.com/voice-ai-development",
                "desc": "Full-duplex multilingual voice AI engines for telecommunications and mobile applications. Equipped with noise cancellation, barge-in interruption detection, and dynamic telephony trunking (Twilio/LiveKit).",
                "keywords": "Voice AI development, speech-to-speech agents, Twilio voice AI, telephony AI automation"
            },
            {
                "slug": "ml-model-deployment",
                "name": "ML Model Deployment & MLOps",
                "url": "https://www.shriramitventures.com/ml-model-deployment",
                "desc": "Containerized model serving using TorchServe, Triton, vLLM, and FastAPI. Automated continuous integration and deployment (CI/CD) with Prometheus drift monitoring, GPU auto-scaling, and A/B traffic split testing.",
                "keywords": "MLOps, ML model deployment, vLLM serving, GPU cluster management, model drift monitoring"
            }
        ]
    },
    {
        "category": "2. 💻 Web, SaaS & Custom Software Engineering",
        "anchor": "2--web-saas--custom-software-engineering",
        "intro": "We design, architect, and construct robust web applications and multi-tenant SaaS products engineered to handle explosive traffic and complex operational workflows. Clean domain-driven architecture, strict tenant isolation, and zero spaghetti code.",
        "services": [
            {
                "slug": "web-development",
                "name": "Web Development",
                "url": "https://www.shriramitventures.com/web-development",
                "desc": "Enterprise web applications built with clean code, sub-second load times, semantic HTML5, and accessibility compliance (WCAG 2.1). Shipped with weekly demo milestones and automated deployment pipelines.",
                "keywords": "custom web development, enterprise web apps, high-performance websites, full stack web engineering"
            },
            {
                "slug": "saas-development",
                "name": "SaaS Platform Development",
                "url": "https://www.shriramitventures.com/saas-development",
                "desc": "Turnkey software-as-a-service architecture from tenancy data models to recurring Stripe/Razorpay billing, seat licensing, automated onboarding funnels, and enterprise audit logs.",
                "keywords": "SaaS development company, B2B SaaS architecture, multi-tenant software, subscription billing platform"
            },
            {
                "slug": "software-development",
                "name": "Enterprise Software Development",
                "url": "https://www.shriramitventures.com/software-development",
                "desc": "Bespoke digital backbones for growing enterprises. We build custom transactional processing engines, inventory ledgers, and distributed systems tailored to your specific operational blueprint.",
                "keywords": "enterprise software development, custom software engineering, scalable business systems"
            },
            {
                "slug": "custom-software-development",
                "name": "Custom Software Development",
                "url": "https://www.shriramitventures.com/custom-software-development",
                "desc": "Purpose-built business platforms that eliminate compromises inherent in off-the-shelf software. We write clean, thoroughly documented code with full intellectual property (IP) transfer.",
                "keywords": "custom software development services, bespoke business software, tailored digital solutions"
            },
            {
                "slug": "multi-tenant-saas",
                "name": "Multi-Tenant SaaS Architecture",
                "url": "https://www.shriramitventures.com/multi-tenant-saas",
                "desc": "Architectural consulting and implementation of database-per-tenant, schema-per-tenant, and row-level security (RLS) data partitioning models ensuring ironclad data isolation across tenants.",
                "keywords": "multi-tenant architecture, SaaS tenant isolation, Row Level Security RLS, cloud tenancy models"
            },
            {
                "slug": "multi-tenant-saas-builds",
                "name": "Multi-Tenant SaaS Platform Builds",
                "url": "https://www.shriramitventures.com/multi-tenant-saas-builds",
                "desc": "End-to-end execution of multi-tenant cloud platforms including tenant provisioning, subdomain routing, usage-based metering, feature flag toggles, and tenant-level backup/restore capabilities.",
                "keywords": "multi-tenant SaaS engineering, SaaS platform builds, tenant onboarding automation"
            },
            {
                "slug": "marketplace-saas",
                "name": "Marketplace SaaS Platforms",
                "url": "https://www.shriramitventures.com/marketplace-saas",
                "desc": "Two-sided and multi-vendor platforms featuring merchant onboarding, split escrow payments, commission calculations, review moderation, and dispute resolution workflows.",
                "keywords": "marketplace SaaS development, two-sided marketplace, multi-vendor SaaS platform"
            },
            {
                "slug": "mvp-development",
                "name": "Rapid Startup MVP Development",
                "url": "https://www.shriramitventures.com/mvp-development",
                "desc": "Structured 8-to-12 week rapid MVP sprints. We strip out unnecessary scope to build a focused, shippable product with production instrumentation ready for investor diligence and early customer traction.",
                "keywords": "MVP development services, startup MVP builder, rapid prototype to production, lean software build"
            },
            {
                "slug": "website-development",
                "name": "High-Performance Website Development",
                "url": "https://www.shriramitventures.com/website-development",
                "desc": "Conversion-focused corporate portals built for maximum organic visibility, 95+ Core Web Vitals, dynamic localization, and rapid editorial content updates without developer dependencies.",
                "keywords": "corporate website development, high-speed business websites, Core Web Vitals optimization"
            },
            {
                "slug": "landing-page-development",
                "name": "High-Converting Landing Page Development",
                "url": "https://www.shriramitventures.com/landing-page-development",
                "desc": "High-velocity landing pages engineered for performance marketing and programmatic campaigns. Built with semantic markup, dynamic content personalization, and instant form-to-CRM webhooks.",
                "keywords": "landing page development, CRO landing pages, high converting web pages, marketing funnels"
            },
            {
                "slug": "progressive-web-apps",
                "name": "Progressive Web Apps (PWA)",
                "url": "https://www.shriramitventures.com/progressive-web-apps",
                "desc": "Offline-capable web applications that install directly onto iOS, Android, and desktop devices. Leverages service workers, IndexedDB caching, and web push notifications without 30% App Store fees.",
                "keywords": "PWA development, progressive web apps, offline web apps, installable web applications"
            },
            {
                "slug": "pwa-development",
                "name": "PWA Engineering & Performance",
                "url": "https://www.shriramitventures.com/pwa-development",
                "desc": "Industrial PWA solutions designed for field technicians and warehouse operators working in low-bandwidth or offline environments, featuring automatic background synchronization on network reconnect.",
                "keywords": "enterprise PWA development, offline-first web apps, service worker engineering"
            },
            {
                "slug": "cms-development",
                "name": "Custom CMS Development",
                "url": "https://www.shriramitventures.com/cms-development",
                "desc": "Custom content management engines tailored to complex editorial publishing workflows, multi-tier approval states, digital asset management, and granular role permissions.",
                "keywords": "custom CMS development, enterprise content management, editorial publishing platform"
            },
            {
                "slug": "headless-cms-development",
                "name": "Headless CMS Architecture & Development",
                "url": "https://www.shriramitventures.com/headless-cms-development",
                "desc": "Modern decoupled architectures pairing Strapi, Sanity, Contentful, or Filament with React/Next.js frontends via GraphQL/REST APIs, ensuring total design flexibility and instant omnichannel distribution.",
                "keywords": "headless CMS development, Strapi development, Sanity CMS, decoupled web architecture"
            },
            {
                "slug": "internal-tools",
                "name": "Internal Tools & Operations Portals",
                "url": "https://www.shriramitventures.com/internal-tools",
                "desc": "Custom administrative dashboards, customer support consoles, inventory adjusters, and audit log viewers that replace brittle Google Sheets with secure, role-restricted web tools.",
                "keywords": "internal tools development, custom admin panels, ops tooling, business portal development"
            },
            {
                "slug": "legacy-modernization",
                "name": "Legacy System Modernization",
                "url": "https://www.shriramitventures.com/legacy-modernization",
                "desc": "Strategic revitalization of aging enterprise systems. We refactor monolithic code, migrate legacy databases to cloud-native engines, and decouple brittle dependencies without disrupting active business operations.",
                "keywords": "legacy system modernization, software re-architecture, monolithic to microservices, database migration"
            },
            {
                "slug": "strangler-migrations",
                "name": "Strangler Fig Pattern Architecture Migrations",
                "url": "https://www.shriramitventures.com/strangler-migrations",
                "desc": "Zero-downtime, incremental replacement of monolithic architectures by systematically intercepting routes with reverse proxies and migrating domain bounded contexts one microservice at a time.",
                "keywords": "strangler fig pattern, incremental system rewrite, zero downtime migration, microservices migration"
            }
        ]
    },
    {
        "category": "3. 📱 Mobile Application Engineering (iOS & Android)",
        "anchor": "3--mobile-application-engineering-ios--android",
        "intro": "We build store-approved, 60fps mobile applications engineered for high engagement, offline stability, and native device performance across iOS and Android.",
        "services": [
            {
                "slug": "mobile-app-development",
                "name": "Mobile App Development",
                "url": "https://www.shriramitventures.com/mobile-app-development",
                "desc": "Full-lifecycle mobile engineering from concept wireframing to App Store / Google Play approval. We build responsive, battery-efficient mobile apps that delight end-users.",
                "keywords": "mobile app development company, iOS and Android apps, custom mobile software, mobile product studio"
            },
            {
                "slug": "ios-app-development",
                "name": "Native iOS App Development",
                "url": "https://www.shriramitventures.com/ios-app-development",
                "desc": "Native iOS applications built with Swift and SwiftUI adhering strictly to Apple Human Interface Guidelines. Deep integration with Apple Pay, HealthKit, PushKit, and CoreML.",
                "keywords": "iOS app development, Swift SwiftUI developer, native iPhone apps, Apple App Store compliance"
            },
            {
                "slug": "flutter-apps",
                "name": "Flutter Cross-Platform App Engineering",
                "url": "https://www.shriramitventures.com/flutter-apps",
                "desc": "High-performance cross-platform mobile apps using Google Flutter. Single codebase rendering native ARM code at 60/120fps with uniform design consistency across platforms.",
                "keywords": "Flutter app development, cross platform Flutter, Dart mobile apps, high performance Flutter"
            },
            {
                "slug": "flutter-app-development",
                "name": "Enterprise Flutter App Development",
                "url": "https://www.shriramitventures.com/flutter-app-development",
                "desc": "Scalable enterprise Flutter apps utilizing BLoC and Riverpod state management, offline SQLite caching, background location telemetry, and secure biometrics authentication.",
                "keywords": "enterprise Flutter development, Flutter BLoC architecture, scalable mobile software"
            },
            {
                "slug": "react-native-apps",
                "name": "React Native Mobile Applications",
                "url": "https://www.shriramitventures.com/react-native-apps",
                "desc": "Cross-platform mobile applications leveraging the React ecosystem. Maximize code reuse between web and mobile interfaces while retaining authentic native feel and responsiveness.",
                "keywords": "React Native development, cross platform React Native, native module bridge, mobile React apps"
            },
            {
                "slug": "react-native-app-development",
                "name": "Production-Grade React Native Development",
                "url": "https://www.shriramitventures.com/react-native-app-development",
                "desc": "Enterprise React Native apps built with Expo, Hermes JavaScript engine, TypeScript strict mode, dynamic code-push updates, and streamlined OTA release cycles.",
                "keywords": "React Native app development services, Expo development, Hermes optimization, mobile CI/CD"
            },
            {
                "slug": "cross-platform-app-development",
                "name": "Unified Cross-Platform App Development",
                "url": "https://www.shriramitventures.com/cross-platform-app-development",
                "desc": "Strategic cross-platform mobile development that balances maximum code reuse with platform-specific idioms, cutting development overhead by up to 40% while preserving user delight.",
                "keywords": "cross-platform mobile apps, multiplatform development, hybrid mobile app engineering"
            },
            {
                "slug": "taxi-app-development",
                "name": "Taxi & Ride-Hailing App Development",
                "url": "https://www.shriramitventures.com/taxi-app-development",
                "desc": "On-demand dispatch platforms featuring passenger booking apps, driver dispatch consoles, live Google/Mapbox turn-by-turn routing, automated fare surge algorithms, and in-app wallet integrations.",
                "keywords": "taxi app development, ride hailing software, on-demand dispatch system, Uber clone architecture"
            },
            {
                "slug": "food-delivery-app-development",
                "name": "Food & Grocery Delivery App Development",
                "url": "https://www.shriramitventures.com/food-delivery-app-development",
                "desc": "Complete three-sided food delivery software ecosystem: customer ordering app, restaurant kitchen display terminal, and courier GPS tracking application with live order state machines.",
                "keywords": "food delivery app development, grocery delivery platform, multi-vendor food delivery software"
            },
            {
                "slug": "healthcare-app-development",
                "name": "Healthcare & Telehealth Mobile App Development",
                "url": "https://www.shriramitventures.com/healthcare-app-development",
                "desc": "HIPAA-aware and GDPR-compliant medical apps featuring doctor video consultations (WebRTC), digital e-prescription downloads, lab test booking, and end-to-end encrypted medical messaging.",
                "keywords": "healthcare mobile app development, telemedicine apps, HIPAA compliant mobile apps, doctor booking app"
            },
            {
                "slug": "ecommerce-app-development",
                "name": "Ecommerce & Retail Mobile App Development",
                "url": "https://www.shriramitventures.com/ecommerce-app-development",
                "desc": "High-conversion shopping apps with personalized product recommendations, one-click Apple Pay/Google Pay checkout, cart abandonment push notifications, and barcode search.",
                "keywords": "ecommerce app development, mobile shopping app, m-commerce platform, retail mobile application"
            },
            {
                "slug": "field-service-apps",
                "name": "Mobile Field Service & Workforce Management Apps",
                "url": "https://www.shriramitventures.com/field-service-apps",
                "desc": "Offline-first mobile tools for field technicians, inspectors, and logistics agents. Features job ticketing, GPS timestamped check-ins, digital signature capture, and offline photo attachments.",
                "keywords": "field service app development, mobile workforce management, offline field technician app"
            },
            {
                "slug": "warehouse-apps",
                "name": "Mobile Warehouse & Barcode Scanner Apps",
                "url": "https://www.shriramitventures.com/warehouse-apps",
                "desc": "High-speed handheld warehouse applications optimized for Zebra and Honeywell scanners. Streamlines pick-pack-ship workflows, bin location tracking, cycle counts, and real-time inventory reconciliation.",
                "keywords": "warehouse mobile app, barcode scanner app, inventory management mobile software, pick pack ship app"
            }
        ]
    },
    {
        "category": "4. ⚡ Framework & Stack Specialists (Laravel, React, Next.js, Node.js)",
        "anchor": "4--framework--stack-specialists-laravel-react-nextjs-nodejs",
        "intro": "We are recognized specialists in the Laravel, React, and modern TypeScript ecosystems. We deliver robust backends, lightning-fast APIs, clean data schemas, and modern server-rendered frontends.",
        "services": [
            {
                "slug": "laravel-development",
                "name": "Laravel Web Application Development",
                "url": "https://www.shriramitventures.com/laravel-development",
                "desc": "Enterprise PHP engineering utilizing modern Laravel (10/11+). Clean MVC architecture, Eloquent ORM performance tuning, Redis queue workers, event listeners, and automated test coverage.",
                "keywords": "Laravel development company, expert Laravel developers, enterprise PHP development, Laravel web apps"
            },
            {
                "slug": "laravel-api-development",
                "name": "High-Throughput Laravel API Development",
                "url": "https://www.shriramitventures.com/laravel-api-development",
                "desc": "Scalable RESTful and GraphQL API backends built on Laravel. Features Sanctum/Passport OAuth2 tokens, granular rate-limiting, sub-100ms response caching, and automated Swagger/OpenAPI documentation.",
                "keywords": "Laravel API development, RESTful APIs Laravel, Laravel microservices, secure API endpoints"
            },
            {
                "slug": "laravel-crm-development",
                "name": "Custom Laravel CRM Development",
                "url": "https://www.shriramitventures.com/laravel-crm-development",
                "desc": "Bespoke Customer Relationship Management software tailored to unique sales pipelines, automated email/WhatsApp sequences, lead scoring models, and role-based operational permissions.",
                "keywords": "Laravel CRM development, custom CRM software, bespoke sales pipeline software"
            },
            {
                "slug": "laravel-erp-development",
                "name": "Scalable Laravel ERP Development",
                "url": "https://www.shriramitventures.com/laravel-erp-development",
                "desc": "Full-scale enterprise resource planning systems handling multi-branch accounting, automated GST/VAT invoicing, inventory batch tracking, vendor purchase orders, and audit ledgers.",
                "keywords": "Laravel ERP development, custom ERP software, business management software, enterprise ERP system"
            },
            {
                "slug": "laravel-saas-development",
                "name": "Multi-Tenant Laravel SaaS Development",
                "url": "https://www.shriramitventures.com/laravel-saas-development",
                "desc": "Cloud multi-tenant SaaS platforms powered by Stancl/Tenancy, Laravel Cashier (Stripe/Paddle), metered usage billing, custom tenant subdomains, and separate tenant database isolation.",
                "keywords": "Laravel SaaS development, multi-tenant Laravel, SaaS boilerplate architecture, subscription billing"
            },
            {
                "slug": "laravel-maintenance",
                "name": "Laravel Maintenance & SLA Support",
                "url": "https://www.shriramitventures.com/laravel-maintenance",
                "desc": "Proactive SLA-backed maintenance for mission-critical Laravel systems. Framework major version upgrades, PHP 8.2+ performance tuning, security patch application, and 24/7 uptime monitoring.",
                "keywords": "Laravel maintenance services, Laravel support retainer, PHP framework upgrade, bug fixing retainer"
            },
            {
                "slug": "laravel-migration",
                "name": "Legacy PHP to Modern Laravel Migration",
                "url": "https://www.shriramitventures.com/laravel-migration",
                "desc": "De-risked migration of outdated legacy PHP monoliths (CodeIgniter, CakePHP, raw PHP, Yii) to modern Laravel architecture, ensuring zero data loss and automated regression verification.",
                "keywords": "Laravel migration services, legacy PHP to Laravel, CodeIgniter to Laravel, framework upgrade"
            },
            {
                "slug": "laravel-security",
                "name": "Laravel Application Security Hardening & Audit",
                "url": "https://www.shriramitventures.com/laravel-security",
                "desc": "Deep vulnerability assessments and hardening covering SQL injection, Mass Assignment, CSRF, insecure direct object references (IDOR), session hijacking, and composer dependency auditing.",
                "keywords": "Laravel security audit, Laravel vulnerability assessment, PHP security hardening, secure code review"
            },
            {
                "slug": "react-development",
                "name": "Enterprise React.js Development",
                "url": "https://www.shriramitventures.com/react-development",
                "desc": "Modular single-page and hybrid web applications engineered with modern React, TypeScript, custom hooks, atomic design principles, and automated Vitest/Jest unit test suites.",
                "keywords": "React development company, hire React developers, TypeScript React apps, single page applications"
            },
            {
                "slug": "react-dashboard-development",
                "name": "Data-Dense React Dashboard Development",
                "url": "https://www.shriramitventures.com/react-dashboard-development",
                "desc": "High-performance operational dashboards capable of rendering millions of live data points using virtualized lists (TanStack Virtual), interactive charts (ECharts/Recharts), and WebSocket feeds.",
                "keywords": "React dashboard development, real-time analytics dashboard, interactive React data visualization"
            },
            {
                "slug": "react-enterprise-apps",
                "name": "High-Availability Enterprise React Apps",
                "url": "https://www.shriramitventures.com/react-enterprise-apps",
                "desc": "Mission-critical enterprise frontend platforms built with micro-frontends, shared npm design tokens, strict state management (Zustand/Redux Toolkit), and fault-tolerant error boundaries.",
                "keywords": "enterprise React applications, micro-frontends React, scalable frontend architecture"
            },
            {
                "slug": "react-admin-panel",
                "name": "Custom React Admin Portals & CMS",
                "url": "https://www.shriramitventures.com/react-admin-panel",
                "desc": "Tailor-made back-office panels, moderation hubs, and content management interfaces built with refine.dev, React Admin, and Tailwind CSS for lightning-fast internal operations.",
                "keywords": "React admin panel, custom back office portal, React content dashboard, internal admin portal"
            },
            {
                "slug": "react-ui-development",
                "name": "Component-Driven React UI Development",
                "url": "https://www.shriramitventures.com/react-ui-development",
                "desc": "Pixel-perfect, accessible (a11y) component libraries constructed with Radix UI, Headless UI, and Tailwind CSS. Built to seamlessly translate complex Figma designs into clean React code.",
                "keywords": "React UI development, headless UI components, Tailwind CSS React, design system components"
            },
            {
                "slug": "react-performance",
                "name": "React Performance Engineering & CWV Optimization",
                "url": "https://www.shriramitventures.com/react-performance",
                "desc": "Eliminating memory leaks, unnecessary re-renders, and bloated bundle sizes. We optimize React rendering trees, lazy-load assets, and achieve 95+ Google Lighthouse performance scores.",
                "keywords": "React performance optimization, Core Web Vitals React, bundle size reduction, React speed audit"
            },
            {
                "slug": "react-seo",
                "name": "Server-Side & Hybrid React SEO Architecture",
                "url": "https://www.shriramitventures.com/react-seo",
                "desc": "Solving client-side rendering SEO blind spots using dynamic pre-rendering, SSR hydration, canonical metadata injectors, and automated XML sitemaps to ensure 100% Google indexing.",
                "keywords": "React SEO optimization, server side rendering SEO, SPA indexing, dynamic prerendering React"
            },
            {
                "slug": "react-with-laravel",
                "name": "Decoupled React Frontend with Laravel Backend",
                "url": "https://www.shriramitventures.com/react-with-laravel",
                "desc": "Best-of-both-worlds architecture pairing an interactive, reactive React/TypeScript frontend with a rock-solid, secure Laravel REST API or Inertia.js bridge.",
                "keywords": "React with Laravel, Laravel React full stack, Inertia.js development, modern web architecture"
            },
            {
                "slug": "nextjs-development",
                "name": "Next.js Full-Stack Web Development",
                "url": "https://www.shriramitventures.com/nextjs-development",
                "desc": "High-performance enterprise web platforms utilizing Next.js App Router, React Server Components (RSC), Incremental Static Regeneration (ISR), and edge caching for sub-second page delivery.",
                "keywords": "Next.js development company, React Server Components, Next.js App Router, SSR web applications"
            },
            {
                "slug": "nodejs-microservices",
                "name": "Distributed Node.js Microservices",
                "url": "https://www.shriramitventures.com/nodejs-microservices",
                "desc": "Event-driven asynchronous microservices architectures built on Node.js, Express, Fastify, and NestJS. Integrated with Redis pub/sub, Apache Kafka, and RabbitMQ message brokers.",
                "keywords": "Node.js microservices, event-driven architecture, NestJS backend, high throughput Node APIs"
            }
        ]
    },
    {
        "category": "5. 🛍️ Ecommerce & Headless Commerce Engineering",
        "anchor": "5--ecommerce--headless-commerce-engineering",
        "intro": "We engineer high-converting digital storefronts and headless commerce engines designed for peak promotional traffic, instant checkout, and frictionless multichannel catalog synchronization.",
        "services": [
            {
                "slug": "ecommerce-development",
                "name": "Custom Ecommerce Development",
                "url": "https://www.shriramitventures.com/ecommerce-development",
                "desc": "Omnichannel online stores tailored for high conversion rates. Features custom product builders, dynamic tax engines, multi-currency support, and real-time inventory management.",
                "keywords": "custom ecommerce development, online shopping platforms, digital commerce engineering"
            },
            {
                "slug": "shopify-plus-development",
                "name": "Enterprise Shopify Plus Development",
                "url": "https://www.shriramitventures.com/shopify-plus-development",
                "desc": "Enterprise store builds on Shopify Plus: bespoke Liquid theme engineering, custom Shopify Functions checkout validation, private app development, and ERP/CRM connectors.",
                "keywords": "Shopify Plus development agency, custom Shopify themes, Shopify Plus checkout extensions"
            },
            {
                "slug": "headless-shopify",
                "name": "Headless Shopify & Hydrogen Storefronts",
                "url": "https://www.shriramitventures.com/headless-shopify",
                "desc": "Blazing-fast headless ecommerce pairing Shopify's robust commerce backend with Next.js/Hydrogen edge frontends via the Storefront API for sub-second page transitions.",
                "keywords": "headless Shopify development, Shopify Hydrogen, Storefront API, modern headless commerce"
            },
            {
                "slug": "woocommerce-development",
                "name": "Scalable WooCommerce Development",
                "url": "https://www.shriramitventures.com/woocommerce-development",
                "desc": "High-performance WooCommerce storefronts optimized to handle catalogs of 50,000+ SKUs with custom checkout flows, payment gateway integrations, and database query optimization.",
                "keywords": "WooCommerce development services, custom WooCommerce store, WooCommerce performance tuning"
            },
            {
                "slug": "marketplace-development",
                "name": "Multi-Vendor Marketplace Platform Development",
                "url": "https://www.shriramitventures.com/marketplace-development",
                "desc": "Multi-vendor digital marketplaces with vendor self-service dashboards, automated commission calculations, escrow payouts, and seller review systems.",
                "keywords": "multi-vendor marketplace development, B2B marketplace platform, vendor portal software"
            },
            {
                "slug": "inventory-systems",
                "name": "Real-Time Inventory & Stock Management Systems",
                "url": "https://www.shriramitventures.com/inventory-systems",
                "desc": "Centralized stock control synchronizing physical stores, warehouses, and online channels with automated reorder triggers, batch tracking, and supplier EDI integration.",
                "keywords": "inventory management software, stock synchronization system, multi-warehouse stock control"
            }
        ]
    },
    {
        "category": "6. ☁️ Cloud Architecture, DevOps & Infrastructure",
        "anchor": "6--cloud-architecture-devops--infrastructure",
        "intro": "We architect, secure, and manage resilient cloud infrastructure across AWS, Google Cloud, and Azure. Built for 99.99% availability, automated self-healing, and aggressive FinOps cost reduction.",
        "services": [
            {
                "slug": "cloud-solutions",
                "name": "Cloud Solutions & Architecture",
                "url": "https://www.shriramitventures.com/cloud-solutions",
                "desc": "Cloud strategy, architectural design, and migration roadmaps for AWS, GCP, and Azure. Engineered for elastic auto-scaling, disaster recovery, and multi-region redundancy.",
                "keywords": "cloud architecture consulting, AWS consulting, multi-cloud strategy, enterprise cloud solutions"
            },
            {
                "slug": "devops-cicd",
                "name": "DevOps & Automated CI/CD Pipelines",
                "url": "https://www.shriramitventures.com/devops-cicd",
                "desc": "Automating software delivery with GitHub Actions, GitLab CI, and ArgoCD. Zero-downtime blue/green and canary deployments with automated regression test gates.",
                "keywords": "DevOps consulting services, CI CD pipeline automation, GitOps deployment, blue green deployment"
            },
            {
                "slug": "kubernetes-consulting",
                "name": "Production Kubernetes (K8s) Consulting",
                "url": "https://www.shriramitventures.com/kubernetes-consulting",
                "desc": "Production-grade container orchestration: cluster setup (EKS/GKE/K3s), Helm chart packaging, ingress controller routing, service mesh (Istio), and autoscaling policies.",
                "keywords": "Kubernetes consulting, container orchestration, K8s cluster management, AWS EKS deployment"
            },
            {
                "slug": "google-cloud-consulting",
                "name": "Google Cloud Platform (GCP) Consulting",
                "url": "https://www.shriramitventures.com/google-cloud-consulting",
                "desc": "Cloud consulting focused on GCP services: Cloud Run serverless microservices, BigQuery analytics, Pub/Sub event streams, Cloud Armor DDoS mitigation, and IAM governance.",
                "keywords": "Google Cloud consulting, GCP architecture, BigQuery data pipelines, Cloud Run serverless"
            },
            {
                "slug": "cloud-security",
                "name": "Cloud Security Architecture & Hardening",
                "url": "https://www.shriramitventures.com/cloud-security",
                "desc": "Zero-trust cloud network architecture: VPC peering, private subnets, security group lockdowns, automated KMS secret rotation, and continuous CSPM compliance auditing.",
                "keywords": "cloud security services, AWS security hardening, cloud compliance guardrails, CSPM audit"
            },
            {
                "slug": "managed-cloud-services",
                "name": "24/7 Managed Cloud Services & FinOps",
                "url": "https://www.shriramitventures.com/managed-cloud-services",
                "desc": "Around-the-clock infrastructure management, operating system security updates, backup recovery testing, and FinOps audits reducing wasted cloud expenditure by 25-40%.",
                "keywords": "managed cloud services, 24/7 infrastructure management, FinOps cloud cost reduction"
            },
            {
                "slug": "infrastructure-automation",
                "name": "Infrastructure as Code (IaC / Terraform)",
                "url": "https://www.shriramitventures.com/infrastructure-automation",
                "desc": "Declarative cloud provisioning with Terraform and Ansible. Maintain identical staging and production environments with automated drift detection and versioned configurations.",
                "keywords": "Infrastructure as Code, Terraform consulting, automated cloud provisioning, Ansible automation"
            },
            {
                "slug": "monitoring-observability",
                "name": "Monitoring & Distributed Observability",
                "url": "https://www.shriramitventures.com/monitoring-observability",
                "desc": "Centralized logs, metrics, and distributed tracing via Prometheus, Grafana, Datadog, and OpenTelemetry. Real-time alerting for anomalies before they affect users.",
                "keywords": "observability consulting, application performance monitoring, Datadog setup, Grafana Prometheus"
            },
            {
                "slug": "performance-engineering",
                "name": "Performance Engineering & High-Load Optimization",
                "url": "https://www.shriramitventures.com/performance-engineering",
                "desc": "Sub-100ms response optimization: database query indexing, Redis caching topologies, edge CDN caching, HTTP/3, and load testing simulating 100,000+ concurrent requests.",
                "keywords": "performance engineering, high load system optimization, database indexing, latency reduction"
            },
            {
                "slug": "qa-automation",
                "name": "Automated QA & End-to-End Testing",
                "url": "https://www.shriramitventures.com/qa-automation",
                "desc": "Automated test suites built with Playwright, Cypress, and k6 baked directly into CI/CD pipelines to guarantee flawless functional reliability on every git push.",
                "keywords": "QA automation services, automated testing pipeline, Playwright end to end testing, load testing"
            }
        ]
    },
    {
        "category": "7. 🛡️ Cybersecurity, Penetration Testing & Compliance",
        "anchor": "7--cybersecurity-penetration-testing--compliance",
        "intro": "We provide defensive cybersecurity engineering, ethical penetration testing, and compliance certification support that protect your critical IP, customer records, and brand trust.",
        "services": [
            {
                "slug": "cybersecurity",
                "name": "Enterprise Cybersecurity Services",
                "url": "https://www.shriramitventures.com/cybersecurity",
                "desc": "Comprehensive digital defense: threat modeling, perimeter protection, endpoint security, attack surface reduction, and customized security policies for scaling businesses.",
                "keywords": "cybersecurity company, enterprise security consulting, digital threat defense, information security"
            },
            {
                "slug": "security-hardening",
                "name": "Infrastructure & Application Security Hardening",
                "url": "https://www.shriramitventures.com/security-hardening",
                "desc": "Linux kernel hardening, SSH key-only access, database firewall isolation, HTTP security headers (CSP, HSTS), and defensive coding against OWASP Top 10 vulnerabilities.",
                "keywords": "security hardening, server OS hardening, OWASP Top 10 mitigation, secure coding guidelines"
            },
            {
                "slug": "penetration-testing",
                "name": "Ethical Hacking & Penetration Testing",
                "url": "https://www.shriramitventures.com/penetration-testing",
                "desc": "Thorough white-box and black-box penetration testing on web apps, mobile apps, and cloud networks to uncover exploit paths before malicious actors exploit them.",
                "keywords": "penetration testing services, ethical hacking company, network penetration testing, web app pen test"
            },
            {
                "slug": "vapt-services",
                "name": "Vulnerability Assessment & Pen Testing (VAPT)",
                "url": "https://www.shriramitventures.com/vapt-services",
                "desc": "Rigorous VAPT audits with executive risk summaries, CVSS score ratings, detailed proof-of-concept exploits, and developer-ready patch validation certificates.",
                "keywords": "VAPT services, vulnerability assessment, security compliance certificate, cyber audit report"
            },
            {
                "slug": "security-audit",
                "name": "Comprehensive Code & Security Audits",
                "url": "https://www.shriramitventures.com/security-audit",
                "desc": "Static application security testing (SAST) and manual code audits of backends, APIs, and smart contracts to catch business logic flaws and third-party dependency vulnerabilities.",
                "keywords": "security audit services, code security review, SAST audit, dependency vulnerability analysis"
            },
            {
                "slug": "soc-services",
                "name": "Security Operations Center (SOC) Engineering",
                "url": "https://www.shriramitventures.com/soc-services",
                "desc": "Setup and operationalization of 24/7 SOC monitoring, automated incident response runbooks, threat intelligence feeds, and rapid isolation protocols.",
                "keywords": "SOC services, security operations center, 24/7 security monitoring, incident response team"
            },
            {
                "slug": "siem-consulting",
                "name": "SIEM Architecture & Log Correlation",
                "url": "https://www.shriramitventures.com/siem-consulting",
                "desc": "Centralized log ingestion and correlation using Splunk, Wazuh, and Elastic Security with automated threshold alerts for anomalous behavior and privilege escalation.",
                "keywords": "SIEM consulting, Wazuh deployment, Splunk architecture, security log correlation"
            },
            {
                "slug": "zero-trust-security",
                "name": "Zero-Trust Architecture Implementation",
                "url": "https://www.shriramitventures.com/zero-trust-security",
                "desc": "Transition from perimeter-based security to zero-trust network access (ZTNA), micro-segmentation, continuous device verification, and least-privilege role boundaries.",
                "keywords": "zero trust security, ZTNA implementation, micro-segmentation, least privilege access"
            },
            {
                "slug": "identity-sso",
                "name": "Enterprise Identity Management & Single Sign-On (SSO)",
                "url": "https://www.shriramitventures.com/identity-sso",
                "desc": "Centralized identity and access management using OAuth2, OIDC, SAML 2.0, Okta, Auth0, and Azure AD with multi-factor authentication (MFA) and automated SCIM provisioning.",
                "keywords": "SSO integration, enterprise identity management, Okta Auth0 integration, SAML 2.0 OAuth2"
            },
            {
                "slug": "gdpr-ready-platforms",
                "name": "GDPR-Ready Platform Architecture",
                "url": "https://www.shriramitventures.com/gdpr-ready-platforms",
                "desc": "Engineering compliance into core software: Data Subject Access Request (DSAR) workflows, automated user data anonymization, consent logging, and EU data residency.",
                "keywords": "GDPR compliance software, DSAR automation, data privacy engineering, cookie consent compliance"
            },
            {
                "slug": "hipaa-aware-builds",
                "name": "HIPAA-Aware Healthcare Software Builds",
                "url": "https://www.shriramitventures.com/hipaa-aware-builds",
                "desc": "Healthcare digital systems architected for Protected Health Information (PHI) compliance: AES-256 encryption at rest, TLS 1.3 in transit, immutable audit logs, and BAA-compliant cloud.",
                "keywords": "HIPAA compliant software, healthcare cybersecurity, PHI data encryption, HIPAA certified hosting"
            },
            {
                "slug": "soc2-delivery-support",
                "name": "SOC 2 Type I & II Delivery Support",
                "url": "https://www.shriramitventures.com/soc2-delivery-support",
                "desc": "Hands-on engineering support for SOC 2 compliance audits: automated evidence collection, access control verification, change management logging, and policy documentation.",
                "keywords": "SOC 2 delivery support, SOC 2 Type II readiness, compliance evidence automation, security controls"
            }
        ]
    },
    {
        "category": "8. 📈 Technical SEO Engineering, Digital Marketing & Growth",
        "anchor": "8--technical-seo-engineering-digital-marketing--growth",
        "intro": "We treat SEO as a first-class engineering discipline. We build high-speed rendering engines, automated programmatic content networks, and deep schema markup that dominate search results.",
        "services": [
            {
                "slug": "digital-marketing",
                "name": "Full-Funnel Digital Marketing",
                "url": "https://www.shriramitventures.com/digital-marketing",
                "desc": "Growth marketing campaigns merging organic search dominance, high-ROI paid acquisition, conversion rate optimization (CRO), and automated customer retention funnels.",
                "keywords": "digital marketing agency, growth marketing, B2B digital acquisition, performance marketing"
            },
            {
                "slug": "seo-services",
                "name": "Organic Search Engine Optimization (SEO)",
                "url": "https://www.shriramitventures.com/seo-services",
                "desc": "Data-backed SEO campaigns focused on high-intent commercial keywords, content architecture, internal linking graphs, and authoritative backlink acquisition.",
                "keywords": "SEO services company, organic search rankings, keyword strategy, high intent SEO"
            },
            {
                "slug": "technical-seo",
                "name": "Comprehensive Technical SEO Audits",
                "url": "https://www.shriramitventures.com/technical-seo",
                "desc": "In-depth crawl audits resolving crawl budget waste, indexation bottlenecks, redirect chains, canonical errors, duplicate content penalties, and sitemap synchronization.",
                "keywords": "technical SEO audit, website crawlability, indexation fixes, canonical optimization"
            },
            {
                "slug": "technical-seo-engineering",
                "name": "Code-Level Technical SEO Engineering",
                "url": "https://www.shriramitventures.com/technical-seo-engineering",
                "desc": "Engineering-level search optimization: sub-second Largest Contentful Paint (LCP), Interaction to Next Paint (INP) fixes, zero Cumulative Layout Shift (CLS), and structured HTML.",
                "keywords": "technical SEO engineering, Core Web Vitals optimization, INP fix, LCP speed optimization"
            },
            {
                "slug": "programmatic-seo-systems",
                "name": "Programmatic SEO Systems & Dynamic Pages",
                "url": "https://www.shriramitventures.com/programmatic-seo-systems",
                "desc": "Building automated programmatic SEO engines that generate thousands of unique, high-quality landing pages from relational datasets that rank for long-tail search intent.",
                "keywords": "programmatic SEO, programmatic content engine, automated landing pages, long tail SEO scale"
            },
            {
                "slug": "local-seo",
                "name": "Hyperlocal SEO & Google Business Optimization",
                "url": "https://www.shriramitventures.com/local-seo",
                "desc": "Dominating the Google Local 3-Pack: Google Business Profile verification, localized NAP citation networks, hyper-local landing pages, and automated review generation.",
                "keywords": "local SEO services, Google Map pack ranking, Google Business Profile optimization, local citations"
            },
            {
                "slug": "geo-optimization",
                "name": "Multi-Region & Geo-Targeted Search Optimization",
                "url": "https://www.shriramitventures.com/geo-optimization",
                "desc": "Global multi-language SEO architecture: hreflang tag validation, geo-specific CDN edge delivery, currency auto-switching, and country-targeted search positioning.",
                "keywords": "geo targeted SEO, international SEO, hreflang optimization, multi-country search ranking"
            },
            {
                "slug": "schema-markup-implementation",
                "name": "Advanced JSON-LD Schema Markup Architecture",
                "url": "https://www.shriramitventures.com/schema-markup-implementation",
                "desc": "Structured data implementation (Organization, LocalBusiness, Service, Product, FAQPage, BreadcrumbList) enabling rich snippets and inclusion in Google Knowledge Graph.",
                "keywords": "schema markup implementation, JSON-LD structured data, rich snippet optimization, Google knowledge graph"
            },
            {
                "slug": "ga4-implementation",
                "name": "Server-Side GA4 Tracking & Analytics",
                "url": "https://www.shriramitventures.com/ga4-implementation",
                "desc": "Server-side Google Tag Manager (sGTM) and Google Analytics 4 tracking. Bypass ad-blockers, maintain 100% conversion attribution, and construct Looker Studio executive dashboards.",
                "keywords": "GA4 implementation, server side GTM, Google Analytics 4 tracking, conversion tracking Looker Studio"
            },
            {
                "slug": "ppc-management",
                "name": "PPC Campaign Management & Bidding Automation",
                "url": "https://www.shriramitventures.com/ppc-management",
                "desc": "High-efficiency pay-per-click management: automated smart bidding rules, negative keyword sculpting, ad copywriting, and landing page split-testing to maximize ROAS.",
                "keywords": "PPC campaign management, paid search marketing, ROAS optimization, pay per click agency"
            },
            {
                "slug": "google-ads-management",
                "name": "Google Ads Performance Max & Search Management",
                "url": "https://www.shriramitventures.com/google-ads-management",
                "desc": "High-intent Google Search, Display, and Performance Max ad management designed to acquire qualified enterprise leads at the lowest possible Customer Acquisition Cost (CAC).",
                "keywords": "Google Ads management, Performance Max campaigns, Google search ads, lower CAC advertising"
            },
            {
                "slug": "meta-ads-management",
                "name": "Meta (Facebook & Instagram) Funnel Advertising",
                "url": "https://www.shriramitventures.com/meta-ads-management",
                "desc": "Full-funnel customer acquisition campaigns across Meta platforms using Conversions API (CAPI) server tracking, dynamic creative testing, and lookalike audience models.",
                "keywords": "Meta ads management, Facebook Instagram ads, Conversions API CAPI, social media paid ads"
            },
            {
                "slug": "social-media-marketing",
                "name": "B2B & B2C Social Media Marketing",
                "url": "https://www.shriramitventures.com/social-media-marketing",
                "desc": "Strategic brand authority engineering across LinkedIn, Twitter/X, and YouTube, positioning founders and brands as undeniable industry thought leaders.",
                "keywords": "social media marketing, B2B LinkedIn growth, tech brand marketing, executive thought leadership"
            }
        ]
    },
    {
        "category": "9. 🎨 UI/UX Design & Product Strategy",
        "anchor": "9--uiux-design--product-strategy",
        "intro": "We craft research-backed, conversion-focused user interfaces and reusable design systems that solve real operational friction and translate effortlessly into production code.",
        "services": [
            {
                "slug": "ui-ux-design",
                "name": "Product UI/UX Design",
                "url": "https://www.shriramitventures.com/ui-ux-design",
                "desc": "User research, journey mapping, wireframing, high-fidelity Figma mockups, and clickable interactive prototypes engineered for intuitive usability and high user retention.",
                "keywords": "UI UX design agency, product design, user interface design, Figma prototypes, UX research"
            },
            {
                "slug": "ui-design-systems",
                "name": "Multi-Platform UI Design Systems",
                "url": "https://www.shriramitventures.com/ui-design-systems",
                "desc": "Tokenized, multi-platform design systems in Figma and code. Standardizes typography, colors, spacing, and reusable components across web, iOS, and Android platforms.",
                "keywords": "UI design systems, Figma component library, design tokens, design system architecture"
            },
            {
                "slug": "product-design-sprints",
                "name": "Agile Product Design Sprints",
                "url": "https://www.shriramitventures.com/product-design-sprints",
                "desc": "Intense 5-day design sprints to clarify product vision, resolve architectural debates, build high-fidelity interactive prototypes, and test directly with real end-users.",
                "keywords": "product design sprint, 5-day design sprint, rapid prototype validation, UX sprint workshop"
            }
        ]
    },
    {
        "category": "10. 🔄 APIs, Automation & Enterprise Integrations",
        "anchor": "10--apis-automation--enterprise-integrations",
        "intro": "We connect disparate software, automate manual workflows, and build resilient API backbones that eliminate data silos and manual data entry.",
        "services": [
            {
                "slug": "custom-api-development",
                "name": "Custom REST, GraphQL & gRPC API Development",
                "url": "https://www.shriramitventures.com/custom-api-development",
                "desc": "High-throughput, fully documented APIs built with OpenAPI/Swagger specifications, JWT authentication, granular rate limiting, and sub-50ms query responses.",
                "keywords": "custom API development, RESTful API design, GraphQL APIs, gRPC microservices, API integration"
            },
            {
                "slug": "erp-integration",
                "name": "Enterprise ERP Integration",
                "url": "https://www.shriramitventures.com/erp-integration",
                "desc": "Bidirectional data synchronization between modern cloud portals and enterprise legacy ERPs including SAP, Oracle, Microsoft Dynamics, NetSuite, and Tally.",
                "keywords": "ERP integration services, SAP connector, Oracle ERP sync, NetSuite integration, Tally API integration"
            },
            {
                "slug": "erp-development",
                "name": "Custom ERP Software Development",
                "url": "https://www.shriramitventures.com/erp-development",
                "desc": "Bespoke Enterprise Resource Planning platforms designed specifically around your supply chain, manufacturing lines, financial ledgers, and workforce scheduling.",
                "keywords": "custom ERP development, enterprise resource planning system, bespoke ERP platform"
            },
            {
                "slug": "pos-development",
                "name": "Cloud Point-of-Sale (POS) Systems",
                "url": "https://www.shriramitventures.com/pos-development",
                "desc": "Cloud-connected POS systems with offline-first billing, barcode scanners, thermal receipt printer integration, payment terminals, and centralized multi-store inventory sync.",
                "keywords": "POS software development, cloud point of sale, retail POS system, restaurant POS software"
            },
            {
                "slug": "payment-gateway-integration",
                "name": "Secure Payment Gateway Integration",
                "url": "https://www.shriramitventures.com/payment-gateway-integration",
                "desc": "PCI-DSS compliant integrations with Stripe, Razorpay, PayPal, Square, Adyen, and regional banking rails. Features automated webhook reconciliation and fraud detection.",
                "keywords": "payment gateway integration, Stripe integration, Razorpay payment gateway, PCI DSS compliance"
            },
            {
                "slug": "whatsapp-business-api",
                "name": "Official WhatsApp Business API Automation",
                "url": "https://www.shriramitventures.com/whatsapp-business-api",
                "desc": "Automated conversational chatbots, transactional alert delivery, order updates, customer support routing, and payment collections on the official WhatsApp Cloud API.",
                "keywords": "WhatsApp Business API, WhatsApp chatbot, automated WhatsApp alerts, conversational commerce"
            },
            {
                "slug": "twilio-automation",
                "name": "Twilio Telephony & Messaging Automation",
                "url": "https://www.shriramitventures.com/twilio-automation",
                "desc": "Programmable cloud communications: automated voice IVR call trees, SMS two-factor verification, outbound broadcast dispatch, and SIP trunking integration.",
                "keywords": "Twilio automation, programmable SMS, Twilio IVR call tree, cloud telephony integration"
            },
            {
                "slug": "workflow-automation",
                "name": "Enterprise Workflow Automation",
                "url": "https://www.shriramitventures.com/workflow-automation",
                "desc": "Automating repetitive business processes across accounting, HR, and fulfillment. Eliminates human manual errors and saves hundreds of hours of manual data entry every month.",
                "keywords": "workflow automation, business process automation, RPA consulting, automated operations"
            },
            {
                "slug": "n8n-make-integrations",
                "name": "n8n & Make.com Low-Code Integrations",
                "url": "https://www.shriramitventures.com/n8n-make-integrations",
                "desc": "Building resilient low-code automation workflows on self-hosted n8n or Make.com, orchestrating webhooks, AI models, cloud databases, and SaaS tools with custom error handling.",
                "keywords": "n8n automation, Make.com integration, self-hosted n8n workflows, low code business automation"
            }
        ]
    },
    {
        "category": "11. 🏭 Vertical Solutions & Industry Platforms",
        "anchor": "11--vertical-solutions--industry-platforms",
        "intro": "We build deep vertical platforms tailored to complex workflows in healthcare, logistics, manufacturing, education, and connected IoT hardware.",
        "services": [
            {
                "slug": "lms-development",
                "name": "Custom Learning Management Systems (LMS)",
                "url": "https://www.shriramitventures.com/lms-development",
                "desc": "Full-featured EdTech and corporate training platforms with video streaming, interactive quizzes, automated certificate generation, SCORM compliance, and student progress tracking.",
                "keywords": "LMS development, custom learning management system, EdTech platform builder, online course software"
            },
            {
                "slug": "telemedicine-platforms",
                "name": "Telemedicine & Virtual Healthcare Platforms",
                "url": "https://www.shriramitventures.com/telemedicine-platforms",
                "desc": "Compliant virtual clinic portals with encrypted WebRTC video consultations, electronic health records (EHR) sync, digital prescription pads, and patient appointment booking.",
                "keywords": "telemedicine platform development, virtual clinic software, doctor patient video consultation"
            },
            {
                "slug": "fintech-onboarding-flows",
                "name": "Fintech Onboarding & KYC/AML Compliance Flows",
                "url": "https://www.shriramitventures.com/fintech-onboarding-flows",
                "desc": "Frictionless financial onboarding funnels featuring automated ID document scanning, biometric facial verification, credit bureau checks, and AML compliance logging.",
                "keywords": "fintech onboarding, digital KYC verification, AML compliance flow, biometric user onboarding"
            },
            {
                "slug": "realtime-dashboards",
                "name": "Real-Time Telemetry & WebSocket Dashboards",
                "url": "https://www.shriramitventures.com/realtime-dashboards",
                "desc": "Ultra-low-latency real-time control panels utilizing WebSockets and Server-Sent Events (SSE) to visualize live trading, factory sensor metrics, or ride-dispatch events.",
                "keywords": "real-time dashboards, WebSocket dashboard, live operational monitoring, SSE live data feed"
            },
            {
                "slug": "notification-platforms",
                "name": "Multi-Channel Notification Dispatch Platforms",
                "url": "https://www.shriramitventures.com/notification-platforms",
                "desc": "Centralized notification dispatch engines prioritizing and routing transactional alerts across push notifications (APNs/FCM), SMS, email (SES), and WhatsApp with failover.",
                "keywords": "notification platform, multi-channel alert dispatcher, push notification engine, transactional alerts"
            },
            {
                "slug": "search-relevance",
                "name": "Search Relevance & Semantic Vector Search",
                "url": "https://www.shriramitventures.com/search-relevance",
                "desc": "Sub-millisecond faceted search engines combining Elasticsearch, Algolia, and vector embeddings to deliver intelligent typo-tolerant, personalized search results.",
                "keywords": "search relevance engineering, Elasticsearch consulting, Algolia integration, semantic search"
            },
            {
                "slug": "ocr-pipelines",
                "name": "Intelligent Document Processing & OCR Pipelines",
                "url": "https://www.shriramitventures.com/ocr-pipelines",
                "desc": "Computer vision pipelines using AWS Textract, Google Document AI, and vision LLMs to extract structured key-value data from invoices, shipping bills, and medical reports.",
                "keywords": "OCR pipeline development, intelligent document processing, automated invoice parsing, Textract"
            },
            {
                "slug": "pdf-generation-systems",
                "name": "High-Volume PDF Generation Systems",
                "url": "https://www.shriramitventures.com/pdf-generation-systems",
                "desc": "Headless Chromium and Node/Rust PDF rendering systems capable of generating thousands of pixel-perfect tax invoices, lab reports, and shipping manifests per minute.",
                "keywords": "PDF generation system, automated invoice PDF, headless Chrome PDF generator, high volume document generator"
            },
            {
                "slug": "image-pipeline-optimization",
                "name": "Dynamic Image Pipelines & Edge CDN Optimization",
                "url": "https://www.shriramitventures.com/image-pipeline-optimization",
                "desc": "Serverless edge image transformation pipelines that dynamically resize, crop, and convert images to WebP/AVIF formats on the fly, reducing media payload bandwidth by up to 75%.",
                "keywords": "image pipeline optimization, dynamic image resizing, WebP AVIF conversion, edge CDN media optimization"
            },
            {
                "slug": "franchise-portals",
                "name": "Multi-Outlet Franchise Management Portals",
                "url": "https://www.shriramitventures.com/franchise-portals",
                "desc": "Multi-tier operational portals for franchise chains: centralized brand asset distribution, inventory requisition approvals, royalty calculation, and store audit checklists.",
                "keywords": "franchise management portal, multi unit franchise software, franchise royalty management"
            },
            {
                "slug": "partner-portals",
                "name": "B2B Partner & Vendor Extranets",
                "url": "https://www.shriramitventures.com/partner-portals",
                "desc": "Secure extranets for distributors, vendors, and affiliates to track purchase orders, download marketing collateral, register deals, and view commission payouts.",
                "keywords": "B2B partner portal, vendor extranet, affiliate management portal, supplier portal software"
            },
            {
                "slug": "iot-dashboards",
                "name": "IoT Device Management & Telemetry Dashboards",
                "url": "https://www.shriramitventures.com/iot-dashboards",
                "desc": "Scalable cloud platforms ingesting MQTT and HTTP telemetry from thousands of connected hardware devices with live alerting, remote firmware OTA updates, and sensor analytics.",
                "keywords": "IoT dashboard development, MQTT telemetry platform, connected device management, industrial IoT software"
            },
            {
                "slug": "fleet-telemetry-ui",
                "name": "Fleet Telemetry & GPS Tracking Platforms",
                "url": "https://www.shriramitventures.com/fleet-telemetry-ui",
                "desc": "Live fleet dispatch consoles with real-time GPS tracking, historical route replays, geofence breach alerts, fuel consumption monitoring, and driver safety behavior scoring.",
                "keywords": "fleet telemetry UI, GPS tracking software, vehicle fleet management, geofencing dispatch platform"
            }
        ]
    }
]
print("Building full README.md...")

technologies = [
    ("Frontend & Mobile", [
        ("React", "https://www.shriramitventures.com/tech-stack/react", "Component-driven web applications and interactive SPAs"),
        ("TypeScript", "https://www.shriramitventures.com/tech-stack/typescript", "Type-safe enterprise JavaScript codebase architecture"),
        ("Next.js", "https://www.shriramitventures.com/tech-stack/nextjs", "Server-side rendering (SSR), Static Generation (SSG), and React Server Components"),
        ("Flutter", "https://www.shriramitventures.com/tech-stack/flutter", "Cross-platform mobile apps for iOS and Android with native performance"),
        ("React Native", "https://www.shriramitventures.com/tech-stack/react-native", "Native mobile apps leveraging React ecosystems and shared codebases"),
        ("Swift", "https://www.shriramitventures.com/tech-stack/swift", "High-performance native iOS applications and Apple device ecosystem"),
        ("Kotlin", "https://www.shriramitventures.com/tech-stack/kotlin", "Modern native Android applications with coroutines and Jetpack Compose"),
        ("Tailwind CSS", "https://www.shriramitventures.com/tech-stack/tailwind-css", "Utility-first design token styling and accessible component primitives"),
        ("Vue.js", "https://www.shriramitventures.com/tech-stack/vue-js", "Progressive frontend framework for fast and lightweight user interfaces"),
        ("Angular", "https://www.shriramitventures.com/tech-stack/angular", "Strict enterprise frontend architecture with TypeScript and dependency injection")
    ]),
    ("Backend & Microservices", [
        ("Laravel", "https://www.shriramitventures.com/tech-stack/laravel", "Elegant enterprise PHP framework for rapid, secure, and robust SaaS backends"),
        ("PHP", "https://www.shriramitventures.com/tech-stack/php", "Modern PHP 8.2+ with strict typing, JIT compilation, and high-performance execution"),
        ("Node.js", "https://www.shriramitventures.com/tech-stack/nodejs", "Event-driven asynchronous JavaScript runtime for high-concurrency services"),
        ("Express", "https://www.shriramitventures.com/tech-stack/express", "Minimalist, unopinionated web framework for Node.js microservices"),
        ("Python", "https://www.shriramitventures.com/tech-stack/python", "Core backend and scientific computing language for AI, data pipelines, and automation"),
        ("FastAPI", "https://www.shriramitventures.com/tech-stack/fastapi", "Modern, asynchronous high-performance Python framework for machine learning APIs"),
        ("Django", "https://www.shriramitventures.com/tech-stack/django", "Batteries-included secure Python web framework for complex data-driven platforms"),
        ("Go", "https://www.shriramitventures.com/tech-stack/go", "Compiled, highly concurrent language for lightweight microservices and network tooling"),
        ("Rust", "https://www.shriramitventures.com/tech-stack/rust", "Memory-safe, zero-cost abstraction systems programming for ultra-high throughput"),
        ("Java", "https://www.shriramitventures.com/tech-stack/java", "Enterprise backend runtime with high-throughput garbage collection"),
        ("Spring Boot", "https://www.shriramitventures.com/tech-stack/spring-boot", "Production-grade microservices framework for robust enterprise systems")
    ]),
    ("Databases, Caching & Search", [
        ("PostgreSQL", "https://www.shriramitventures.com/tech-stack/postgresql", "Advanced relational database with JSONB support and Row-Level Security (RLS)"),
        ("MySQL", "https://www.shriramitventures.com/tech-stack/mysql", "Battle-tested relational database optimized for web transactions and read replicas"),
        ("Redis", "https://www.shriramitventures.com/tech-stack/redis", "In-memory data store for caching, pub/sub queues, and rate-limiting counters"),
        ("MongoDB", "https://www.shriramitventures.com/tech-stack/mongodb", "Document-oriented NoSQL database for flexible data schemas and rapid iteration"),
        ("Elasticsearch", "https://www.shriramitventures.com/tech-stack/elasticsearch", "Distributed full-text search and analytical log exploration engine"),
        ("Firebase", "https://www.shriramitventures.com/tech-stack/firebase", "Real-time NoSQL database, auth, and cloud functions for rapid prototype syncing"),
        ("Vector DBs", "https://www.shriramitventures.com/tech-stack/vector-dbs", "Specialized vector stores (Pinecone, Qdrant, Chroma, pgvector) for AI embeddings")
    ]),
    ("AI, LLMs & Agentic Systems", [
        ("OpenAI", "https://www.shriramitventures.com/tech-stack/openai", "GPT-4o, reasoning models, and embeddings integration via official APIs"),
        ("Claude / Anthropic", "https://www.shriramitventures.com/tech-stack/claude", "Claude 3.5 Sonnet and Haiku integration for coding and complex analytical reasoning"),
        ("Gemini", "https://www.shriramitventures.com/tech-stack/gemini", "Google Gemini multimodal models with long context window capabilities"),
        ("LangChain", "https://www.shriramitventures.com/tech-stack/langchain", "Framework for building context-aware, reasoning LLM applications"),
        ("LangGraph", "https://www.shriramitventures.com/tech-stack/langgraph", "Cyclic multi-agent orchestrator for robust, controllable autonomous agents"),
        ("Model Context Protocol (MCP)", "https://www.shriramitventures.com/tech-stack/mcp", "Standardized protocol connecting LLMs with private data sources and APIs"),
        ("RAG Pipelines", "https://www.shriramitventures.com/tech-stack/rag-pipelines", "Hybrid retrieval-augmented generation pipelines with reranking algorithms")
    ]),
    ("Cloud, DevOps & Containers", [
        ("AWS", "https://www.shriramitventures.com/tech-stack/aws", "Full AWS ecosystem: EC2, ECS, Lambda, S3, RDS, CloudFront, and IAM security"),
        ("Azure", "https://www.shriramitventures.com/tech-stack/azure", "Microsoft Azure cloud services, Azure App Services, and Active Directory integration"),
        ("Docker", "https://www.shriramitventures.com/tech-stack/docker", "Containerization of applications for reproducible environments across dev and prod"),
        ("Kubernetes", "https://www.shriramitventures.com/tech-stack/kubernetes", "Automated container orchestration, autoscaling, self-healing, and ingress routing"),
        ("Terraform", "https://www.shriramitventures.com/tech-stack/terraform", "Infrastructure as Code (IaC) to version and automate multi-cloud deployments"),
        ("GitHub Actions", "https://www.shriramitventures.com/tech-stack/github-actions", "Continuous Integration and Continuous Deployment (CI/CD) pipelines"),
        ("Jenkins", "https://www.shriramitventures.com/tech-stack/jenkins", "Extensible open-source automation server for complex enterprise deployment pipelines")
    ]),
    ("Commerce, APIs & Analytics", [
        ("Shopify", "https://www.shriramitventures.com/tech-stack/shopify", "Custom Liquid storefronts, private Shopify apps, and Storefront API integrations"),
        ("WooCommerce", "https://www.shriramitventures.com/tech-stack/woocommerce", "Custom WordPress ecommerce development with optimized checkout funnels"),
        ("Stripe", "https://www.shriramitventures.com/tech-stack/stripe", "Payment processing, recurring subscriptions, Stripe Connect marketplace payouts"),
        ("Algolia", "https://www.shriramitventures.com/tech-stack/algolia", "Hosted search-as-a-service engine delivering instant typo-tolerant search results"),
        ("Google Analytics 4 (GA4)", "https://www.shriramitventures.com/tech-stack/ga4", "Server-side and client-side conversion tracking and event attribution"),
        ("Looker Studio", "https://www.shriramitventures.com/tech-stack/looker-studio", "Executive business intelligence reporting and multi-channel marketing dashboards"),
        ("RabbitMQ", "https://www.shriramitventures.com/tech-stack/rabbitmq", "AMQP message broker for reliable asynchronous task queue processing"),
        ("Apache Kafka", "https://www.shriramitventures.com/tech-stack/kafka", "High-throughput distributed event streaming platform for real-time data pipelines"),
        ("GraphQL", "https://www.shriramitventures.com/tech-stack/graphql", "Query language for APIs offering declarative data fetching and schema safety"),
        ("REST API", "https://www.shriramitventures.com/tech-stack/rest-api", "Industry-standard stateless architectural style for web and mobile services")
    ])
]

readme_md = []

# Title & Badges
readme_md.append("# Shriram IT Ventures — Full-Lifecycle Product Engineering, AI Solutions, SaaS, Mobile & Cloud Architecture")
readme_md.append("")
readme_md.append("[![Company Website](https://img.shields.io/badge/Website-shriramitventures.com-0f0b14?style=for-the-badge&logo=google-chrome&logoColor=white)](https://www.shriramitventures.com/) "
                 "[![Headquarters](https://img.shields.io/badge/HQ-Greater%20Noida%2C%20Delhi%20NCR-db2777?style=for-the-badge&logo=google-maps&logoColor=white)](https://www.shriramitventures.com/locations) "
                 "[![Founded](https://img.shields.io/badge/Founded-2019-7c3aed?style=for-the-badge)](https://www.shriramitventures.com/about-us) "
                 "[![Clutch Verified](https://img.shields.io/badge/Clutch-5.0%20%E2%98%85-ea580c?style=for-the-badge&logo=clutch&logoColor=white)](https://clutch.co/profile/shriram-it-ventures) "
                 "[![GoodFirms](https://img.shields.io/badge/GoodFirms-Top%20Rated-2563eb?style=for-the-badge)](https://www.goodfirms.co/company/shriram-it-ventures) "
                 "[![G2 Verified](https://img.shields.io/badge/G2-Verified%20Vendor-f97316?style=for-the-badge&logo=g2&logoColor=white)](https://www.g2.com/products/shriram-it-ventures/reviews) "
                 "[![GitHub](https://img.shields.io/badge/GitHub-shriramitventures-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shriramitventures) "
                 "[![Delivery Standard](https://img.shields.io/badge/Delivery-Weekly%20Demos%20%E2%80%A2%20Strict%20Mode-10b981?style=for-the-badge)](https://www.shriramitventures.com/our-process)")
readme_md.append("")
readme_md.append("> **Welcome to the official technology directory and technical overview for [Shriram IT Ventures](https://www.shriramitventures.com/).**  ")
readme_md.append("> We are a premier product engineering and custom software development company based in **Greater Noida (Delhi NCR), India**, shipping production software, multi-tenant SaaS platforms, autonomous AI features, high-performance mobile apps, and enterprise cloud systems for startups and scaling enterprises across the **United States, United Kingdom, United Arab Emirates (Dubai), Canada, Australia, and India**.")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Table of Contents
readme_md.append("## 📌 Table of Contents")
readme_md.append("")
readme_md.append("- [🏢 About Shriram IT Ventures](#-about-shriram-it-ventures)")
readme_md.append("- [💎 Why Global Teams Choose Us (Our Delivery Ethos)](#-why-global-teams-choose-us-our-delivery-ethos)")
readme_md.append("- [🚀 Complete Directory of 126 Tech Services](#-complete-directory-of-126-tech-services)")
for cat in services_data:
    readme_md.append(f"  - [{cat['category']}](#{cat['anchor']})")
readme_md.append("- [🛠️ Full Technology Stack Matrix (56 Core Technologies)](#️-full-technology-stack-matrix-56-core-technologies)")
readme_md.append("- [📦 Pre-Engineered Enterprise Solutions](#-pre-engineered-enterprise-solutions)")
readme_md.append("- [🌐 Vertical Industry Specializations](#-vertical-industry-specializations)")
readme_md.append("- [🏆 Proven Client Case Studies & Production Portfolios](#-proven-client-case-studies--production-portfolios)")
readme_md.append("- [💬 Client Endorsements & Verified Testimonials](#-client-endorsements--verified-testimonials)")
readme_md.append("- [⚙️ Engagement Models & Engineering Standards](#️-engagement-models--engineering-standards)")
readme_md.append("- [🔍 Search Engine Optimization (SEO) & Knowledge Graph Entities](#-search-engine-optimization-seo--knowledge-graph-entities)")
readme_md.append("- [❓ Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)")
readme_md.append("- [📞 Contact Channels & Global Office Locations](#-contact-channels--global-office-locations)")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# About
readme_md.append("## 🏢 About Shriram IT Ventures")
readme_md.append("")
readme_md.append("Founded in **2019**, **Shriram IT Ventures** is a product engineering company built to replace traditional agency theater with work you can verify: clean architecture, interfaces staff will open on a busy Monday, and content systems that earn organic demand instead of renting it.")
readme_md.append("")
readme_md.append("Headquartered in **Greater Noida (Delhi NCR)** with an engineering studio in **Aligarh**, we combine product strategy, full-stack development, agentic AI engineering, and technical SEO into unified delivery sprints. We partner with founders, CTOs, and enterprise leaders who need working software shipped on time, without sales decks or endless budget adjustments.")
readme_md.append("")
readme_md.append("### Company Credentials & Key Facts")
readme_md.append("- **Official Website**: [https://www.shriramitventures.com/](https://www.shriramitventures.com/)")
readme_md.append("- **Year Established**: 2019")
readme_md.append("- **Headquarters**: Ajnara Homes, Greater Noida, Uttar Pradesh 201304, Delhi NCR, India")
readme_md.append("- **Registered Office**: Rambag Colony Gali No 6, Ramghat Road, Aligarh, Uttar Pradesh 202001, India")
readme_md.append("- **Primary Phone**: [+91 95484 81594](tel:+919548481594)")
readme_md.append("- **Official Email**: [info@shriramitventures.com](mailto:info@shriramitventures.com)")
readme_md.append("- **Geographic Coverage**: United States, United Kingdom, United Arab Emirates (Dubai / Abu Dhabi), Canada, Australia, and India")
readme_md.append("- **Core Team Leadership**: Satyendra Pal Singh (Owner), Vikas Kumar (CEO), Praveen Rajpoot (Technical Lead / Solutions Architect)")
readme_md.append("- **Direct Profile Directories**: [Clutch Profile](https://clutch.co/profile/shriram-it-ventures) • [GoodFirms](https://www.goodfirms.co/company/shriram-it-ventures) • [G2 Reviews](https://www.g2.com/products/shriram-it-ventures/reviews) • [Google Reviews](https://share.google/uHG8F632J36RhvVme)")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Why Choose Us
readme_md.append("## 💎 Why Global Teams Choose Us (Our Delivery Ethos)")
readme_md.append("")
readme_md.append("| Traditional Dev Agency Theater | The Shriram IT Ventures Standard |")
readme_md.append("| :--- | :--- |")
readme_md.append("| **Sales Decks & Vague Retainers** | **Written Scope & Honest Estimates** scoped during discovery before contracts are signed. |")
readme_md.append("| **Monthly Slide Decks with No Working Code** | **Weekly Working Software Demos Every Friday** deployed to dedicated staging links. |")
readme_md.append("| **SEO Bolted On After Launch as an Afterthought** | **Technical SEO Engineered into Code** (JSON-LD schema, SSR, CWV, 301 redirection maps). |")
readme_md.append("| **Fragile Codebases Requiring Costly Rewrites** | **TypeScript Strict Mode & Comprehensive Test Suites** designed for years of reliable scale. |")
readme_md.append("| **Junior Developers Hidden Behind Account Managers** | **Direct Collaboration with Senior Engineers** via dedicated Slack/Discord squads. |")
readme_md.append("| **Vendor Lock-in & Proprietary Frameworks** | **100% Client Ownership** of code repositories, CI/CD runbooks, and cloud accounts. |")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Catalog of 126 Services
readme_md.append("## 🚀 Complete Directory of 126 Tech Services")
readme_md.append("")
readme_md.append("Below is the comprehensive, indexed catalog of all **126 technical services and engineering capabilities** offered by Shriram IT Ventures. Every service is linked directly to its authoritative canonical page on [shriramitventures.com](https://www.shriramitventures.com/).")
readme_md.append("")

for cat_idx, cat in enumerate(services_data, 1):
    readme_md.append(f"### {cat['category']}")
    readme_md.append("")
    readme_md.append(f"*{cat['intro']}*")
    readme_md.append("")
    readme_md.append("| # | Service Name & Link | Technical Scope & Production Deliverables | Target Keyword Focus |")
    readme_md.append("| :-: | :--- | :--- | :--- |")
    for s_idx, s in enumerate(cat['services'], 1):
        readme_md.append(f"| {s_idx} | [**{s['name']}**]({s['url']}) | {s['desc']} | `{s['keywords']}` |")
    readme_md.append("")

readme_md.append("---")
readme_md.append("")

# Technology Stack Matrix
readme_md.append("## 🛠️ Full Technology Stack Matrix (56 Core Technologies)")
readme_md.append("")
readme_md.append("We pick technologies based on hiring market depth, long-term ecosystem stability, and operational reality — not fleeting Twitter trends. Below is our verified stack catalog indexed on [shriramitventures.com/tech-stack](https://www.shriramitventures.com/tech-stack):")
readme_md.append("")

for domain_name, tech_list in technologies:
    readme_md.append(f"### 🔹 {domain_name}")
    readme_md.append("")
    readme_md.append("| Technology | Documentation & URL | Engineering Role & Operational Use Case |")
    readme_md.append("| :--- | :--- | :--- |")
    for t_name, t_url, t_desc in tech_list:
        readme_md.append(f"| **{t_name}** | [{t_name} Overview]({t_url}) | {t_desc} |")
    readme_md.append("")

readme_md.append("---")
readme_md.append("")

# Pre-Engineered Enterprise Solutions
readme_md.append("## 📦 Pre-Engineered Enterprise Solutions")
readme_md.append("")
readme_md.append("In addition to bespoke software builds, Shriram IT Ventures maintains battle-tested, modular software kits that accelerate time-to-market by 40–60%. Explore our specialized solutions catalog on [shriramitventures.com/solutions](https://www.shriramitventures.com/solutions):")
readme_md.append("")
readme_md.append("- **Enterprise CRM Suites**: Tailored CRM solutions for [Hospitals](https://www.shriramitventures.com/solutions/crm-for-hospitals), [Clinics](https://www.shriramitventures.com/solutions/crm-for-clinics), [Pharmacies](https://www.shriramitventures.com/solutions/crm-for-pharmacies), [Schools](https://www.shriramitventures.com/solutions/crm-for-schools), [Universities](https://www.shriramitventures.com/solutions/crm-for-universities), [Manufacturers](https://www.shriramitventures.com/solutions/crm-for-manufacturers), [Warehouses](https://www.shriramitventures.com/solutions/crm-for-warehouses), and [Logistics Firms](https://www.shriramitventures.com/solutions/crm-for-logistics-firms).")
readme_md.append("- **Custom ERP Systems**: End-to-end ERP platforms for [Manufacturing](https://www.shriramitventures.com/solutions/erp-for-manufacturing), [Hospitals](https://www.shriramitventures.com/solutions/erp-for-hospitals), [Clinics](https://www.shriramitventures.com/solutions/erp-for-clinics), [Pharmacies](https://www.shriramitventures.com/solutions/erp-for-pharmacies), [Schools](https://www.shriramitventures.com/solutions/school-erp), [Universities](https://www.shriramitventures.com/solutions/erp-for-universities), [Warehouses](https://www.shriramitventures.com/solutions/erp-for-warehouses), and [Logistics Firms](https://www.shriramitventures.com/solutions/erp-for-logistics-firms).")
readme_md.append("- **Learning Management Systems (LMS)**: Specialized LMS portals for [Hospitals](https://www.shriramitventures.com/solutions/lms-for-hospitals), [Clinics](https://www.shriramitventures.com/solutions/lms-for-clinics), [Schools](https://www.shriramitventures.com/solutions/lms-for-schools), [Universities](https://www.shriramitventures.com/solutions/lms-for-universities), and [Industrial Manufacturers](https://www.shriramitventures.com/solutions/lms-for-manufacturers).")
readme_md.append("- **Hospital Information Systems (HIS)**: Digital clinical records, inpatient/outpatient management, pharmacy billing, and diagnostic lab sync for [Hospitals](https://www.shriramitventures.com/solutions/his-for-hospitals) and [Clinics](https://www.shriramitventures.com/solutions/his-for-clinics).")
readme_md.append("- **Point of Sale (POS) Systems**: Multi-outlet cloud-connected POS with offline cash billing and inventory synchronization for [Pharmacies](https://www.shriramitventures.com/solutions/pos-for-pharmacies), [Clinics](https://www.shriramitventures.com/solutions/pos-for-clinics), and [Retail Warehouses](https://www.shriramitventures.com/solutions/pos-for-warehouses).")
readme_md.append("- **Warehouse Management Systems (WMS)**: Barcode/RFID-enabled stock intake, bin location allocation, picking paths, and dispatch validation for [Warehouses](https://www.shriramitventures.com/solutions/wms-for-warehouses) and [3PL Logistics](https://www.shriramitventures.com/solutions/wms-for-logistics-firms).")
readme_md.append("- **WhatsApp Automation Platform**: [Official WhatsApp Business API platform](https://www.shriramitventures.com/solutions/whatsapp-automation-platform) for automated conversational commerce, broadcast alerts, appointment reminders, and support ticket routing.")
readme_md.append("- **Fleet Management Software**: [Vehicle tracking and telemetry platform](https://www.shriramitventures.com/solutions/fleet-management-software) with real-time GPS coordinates, geofence trigger alerts, and fuel consumption analytics.")
readme_md.append("- **Restaurant Online Ordering System**: [Commission-free food ordering solution](https://www.shriramitventures.com/solutions/restaurant-ordering-system) with kitchen display terminals, table QR code billing, and delivery dispatch.")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Industry Verticals
readme_md.append("## 🌐 Vertical Industry Specializations")
readme_md.append("")
readme_md.append("Software only succeeds when it respects industry-specific regulatory constraints and operational nuances. Discover our dedicated vertical practice areas on [shriramitventures.com/industries](https://www.shriramitventures.com/industries):")
readme_md.append("")
readme_md.append("- 🏥 **Healthcare & Life Sciences**: [Healthcare](https://www.shriramitventures.com/industries/healthcare) • [Hospitals](https://www.shriramitventures.com/industries/hospitals) • [Clinics](https://www.shriramitventures.com/industries/clinics) • [Diagnostics Labs](https://www.shriramitventures.com/industries/diagnostics-labs) • [Pharmacies](https://www.shriramitventures.com/industries/pharmacies) • [Dental Chains](https://www.shriramitventures.com/industries/dental-chains)")
readme_md.append("- 🏭 **Industrial & Manufacturing**: [Manufacturing](https://www.shriramitventures.com/industries/manufacturing) • [Automotive Parts](https://www.shriramitventures.com/industries/automotive-parts) • [Textiles](https://www.shriramitventures.com/industries/textiles) • [Food Processing](https://www.shriramitventures.com/industries/food-processing) • [Electronics Assembly](https://www.shriramitventures.com/industries/electronics-assembly)")
readme_md.append("- 🚚 **Logistics, Freight & Supply Chain**: [3PL Logistics](https://www.shriramitventures.com/industries/3pl) • [Freight Forwarding](https://www.shriramitventures.com/industries/freight-forwarding) • [Last-Mile Delivery](https://www.shriramitventures.com/industries/last-mile-delivery) • [Cold Chain Logistics](https://www.shriramitventures.com/industries/cold-chain)")
readme_md.append("- 🎓 **Education & EdTech**: [Education](https://www.shriramitventures.com/industries/education) • [K-12 Schools](https://www.shriramitventures.com/industries/k-12-schools) • [Higher Education](https://www.shriramitventures.com/industries/higher-education) • [EdTech Platforms](https://www.shriramitventures.com/industries/edtech) • [Coaching Institutes](https://www.shriramitventures.com/industries/coaching-institutes)")
readme_md.append("- 💳 **FinTech & Financial Services**: [FinTech](https://www.shriramitventures.com/industries/fintech) • [NBFC Systems](https://www.shriramitventures.com/industries/nbfc) • [Payment Gateways](https://www.shriramitventures.com/industries/payments) • [InsurTech](https://www.shriramitventures.com/industries/insurtech) • [WealthTech](https://www.shriramitventures.com/industries/wealthtech)")
readme_md.append("- 🛍️ **Retail, Ecommerce & D2C**: [Ecommerce](https://www.shriramitventures.com/industries/ecommerce) • [D2C Brands](https://www.shriramitventures.com/industries/d2c-brands) • [Grocery Chains](https://www.shriramitventures.com/industries/grocery) • [Fashion Retail](https://www.shriramitventures.com/industries/fashion-retail) • [Electronics Retail](https://www.shriramitventures.com/industries/electronics-retail)")
readme_md.append("- 🏢 **PropTech & Real Estate**: [PropTech](https://www.shriramitventures.com/industries/proptech) • [Property Management](https://www.shriramitventures.com/industries/property-management) • [Construction Management](https://www.shriramitventures.com/industries/construction)")
readme_md.append("- 🏨 **Hospitality & Travel**: [Hotels & Resorts](https://www.shriramitventures.com/industries/hotels) • [Restaurants](https://www.shriramitventures.com/industries/restaurants) • [Cloud Kitchens](https://www.shriramitventures.com/industries/cloud-kitchens) • [QSR Chains](https://www.shriramitventures.com/industries/qsr-chains) • [Travel & OTAs](https://www.shriramitventures.com/industries/travel) • [Tour Operators](https://www.shriramitventures.com/industries/tour-operators)")
readme_md.append("- 🤝 **Non-Profit & Public Sector**: [NGOs](https://www.shriramitventures.com/industries/ngos) • [Charitable Foundations](https://www.shriramitventures.com/industries/foundations) • [Social Enterprises](https://www.shriramitventures.com/industries/social-enterprises)")
readme_md.append("- ⚖️ **Professional Services**: [SaaS Companies](https://www.shriramitventures.com/industries/saas) • [B2B Marketplaces](https://www.shriramitventures.com/industries/b2b-marketplaces) • [LegalTech](https://www.shriramitventures.com/industries/legaltech) • [HRTech](https://www.shriramitventures.com/industries/hrtech)")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Case Studies
readme_md.append("## 🏆 Proven Client Case Studies & Production Portfolios")
readme_md.append("")
readme_md.append("We stand behind work that has survived contact with real paying users. Review our selected client case studies on [shriramitventures.com/portfolio](https://www.shriramitventures.com/portfolio):")
readme_md.append("")
readme_md.append("1. **[Ishifo Ethnic Fashion Ecommerce](https://www.shriramitventures.com/portfolio/ishifo-ethnic-fashion-ecommerce)**: Delivered high-conversion ethnic apparel retail storefront with sub-second image loading, automated inventory sync, and seamless checkout.")
readme_md.append("2. **[Manthan Fashion Marketplace](https://www.shriramitventures.com/portfolio/manthan-fashion-marketplace)**: Built multi-vendor ethnic marketplace featuring vendor self-onboarding, commission splits, and responsive mobile catalogs.")
readme_md.append("3. **[SecuroAi Cybersecurity SaaS Platform](https://www.shriramitventures.com/portfolio/securoai-cybersecurity-saas)**: Engineered multi-tenant compliance SaaS platform featuring automated vulnerability reporting, tenant isolation, and audit logging.")
readme_md.append("4. **[Lifecare Navada Healthcare Portal](https://www.shriramitventures.com/portfolio/lifecare-navada-healthcare-website)**: HIPAA-aware clinical portal with patient appointment scheduling, bilingual content expansion, and fast doctor consultation booking.")
readme_md.append("5. **[PartyPlug On-Demand Event Booking](https://www.shriramitventures.com/portfolio)**: High-speed fixed-scope mobile web platform delivered in 8 weeks with real-time vendor slot reservation.")
readme_md.append("6. **[Political Engineer Campaign & Strategy Platform](https://www.shriramitventures.com/portfolio/political-engineer-campaign-platform)**: High-concurrency strategy platform handling dynamic demographic data feeds and voter sentiment analysis during election cycles.")
readme_md.append("7. **[Serenity Villa Luxury Hospitality Portal](https://www.shriramitventures.com/portfolio)**: Luxury booking portal featuring interactive room selection, payment gateway integrations, and mobile-optimized reservation UX.")
readme_md.append("8. **[LodhiRajputShadi Community Matrimonial Platform](https://www.shriramitventures.com/portfolio/lodhirajputshadi-matrimonial-platform)**: High-volume matchmaking platform with profile verification workflows, advanced privacy controls, and search-indexed matrimony landing pages.")
readme_md.append("9. **Enterprise Manufacturing & Security Clients**: Trusted technology partner for **Arme Locks**, **Jyoti Locks**, **Navkiran Netralaya**, **Unique NGO**, **Soul Academy**, and **Technical Avengers**.")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Testimonials
readme_md.append("## 💬 Client Endorsements & Verified Testimonials")
readme_md.append("")
readme_md.append("> *“Shriram IT Ventures treated Ishifo like a product, not a brochure site — weekly demos, clear ownership, and a launch that held up once real users showed up.”*  ")
readme_md.append("> **— Ananya Mehra**, Founder · *Ishifo*")
readme_md.append("")
readme_md.append("> *“They understood clinic realities — appointments, trust, and Hindi content — without turning the project into agency theater.”*  ")
readme_md.append("> **— Dr. Kavita Nair**, Administrator · *Lifecare Navada*")
readme_md.append("")
readme_md.append("> *“PartyPlug needed to ship fast. Shriram’s fixed-scope approach and Friday demos meant we always knew what was live vs next.”*  ")
readme_md.append("> **— Vivek Sharma**, Founder · *PartyPlug*")
readme_md.append("")
readme_md.append("> *“Our fashion catalog needed to look right and still load on mobile. The Greater Noida squad shipped both — and we could edit collections without breaking the layout.”*  ")
readme_md.append("> **— Rohit Manthan**, Director · *Manthan Fashion*")
readme_md.append("")
readme_md.append("> *“AI marketing sites usually overpromise. Shriram kept SecuroAi honest: clear architecture, evals talk for later phases, and a site ops can update.”*  ")
readme_md.append("> **— Arjun Desai**, Product Lead · *SecuroAi*")
readme_md.append("")
readme_md.append("> *“Matrimony traffic is unforgiving. Shriram rebuilt our flows with sensible SEO and pages families could actually complete on a phone.”*  ")
readme_md.append("> **— Suresh Lodhi**, Operator · *LodhiRajputShadi*")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Engagement Models
readme_md.append("## ⚙️ Engagement Models & Engineering Standards")
readme_md.append("")
readme_md.append("We offer flexible engagement formats adapted to where you are in your product lifecycle:")
readme_md.append("")
readme_md.append("### 1. Discovery Sprints (1–2 Weeks)")
readme_md.append("- **Purpose**: De-risk architectural choices, clarify edge cases, and define written scope.")
readme_md.append("- **Deliverables**: System architecture diagram, database schema draft, API contract specs, high-fidelity Figma wireframes, and an honest fixed-cost estimate.")
readme_md.append("")
readme_md.append("### 2. Fixed-Scope MVP Delivery (8–16 Weeks)")
readme_md.append("- **Purpose**: Build and launch an investor-ready, production-grade product on an agreed timeline and budget.")
readme_md.append("- **Deliverables**: Working software demoed every Friday, automated CI/CD pipelines, staging environments, comprehensive unit/integration test coverage, and final App Store/cloud deployment.")
readme_md.append("")
readme_md.append("### 3. Dedicated Product Squads (Monthly Retainer)")
readme_md.append("- **Purpose**: Autonomous, cross-functional engineering pods that scale your existing development capacity.")
readme_md.append("- **Composition**: Senior Full-Stack Engineers (Laravel/React/Next.js/Flutter), AI Engineer, UI/UX Designer, QA Automation Engineer, and Technical Delivery Lead.")
readme_md.append("")
readme_md.append("### Our Engineering Standards")
readme_md.append("1. **Strict TypeScript & Clean Code**: We enforce strict type checking and linting to catch bugs at compile-time.")
readme_md.append("2. **Zero Agency Theater**: No 50-page PowerPoint decks. We communicate via working code, PR diffs, and screen recordings.")
readme_md.append("3. **Automated Testing Gates**: Every pull request must pass automated unit, integration, and security checks before merge.")
readme_md.append("4. **Core Web Vitals Obsession**: We engineer frontends to hit 90+ Lighthouse scores for LCP, INP, and CLS out of the box.")
readme_md.append("5. **100% IP Transfer**: You own all source code, git histories, documentation, and cloud infrastructure from day one.")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# SEO Authority
readme_md.append("## 🔍 Search Engine Optimization (SEO) & Knowledge Graph Entities")
readme_md.append("")
readme_md.append("### High-Intent Search Keyword Targets")
readme_md.append("To ensure search engines understand our exact entity footprint and regional authority, we target the following semantic keyword clusters:")
readme_md.append("")
readme_md.append("- **Primary Entity Keywords**: `Product Engineering Company`, `Custom Software Development Company`, `AI Development Company`, `SaaS Development Company`, `Mobile App Development Company`, `Full Stack Engineering Studio`")
readme_md.append("- **Geographic Authority Keywords**: `Product Engineering Greater Noida`, `Software Development Company Delhi NCR`, `Custom Software Developers Noida`, `IT Services Company Uttar Pradesh`, `Offshore Software Development India to US/UK/UAE`")
readme_md.append("- **Technology Specialist Keywords**: `Laravel Development Company`, `React.js Development Agency`, `Next.js Development Studio`, `Flutter App Development Company`, `Model Context Protocol MCP Server Developers`, `Enterprise RAG System Architects`")
readme_md.append("- **Regulatory & Compliance Keywords**: `HIPAA Compliant Software Development`, `GDPR Ready Web Platforms`, `SOC 2 Delivery Engineering`, `VAPT Security Audit Services`")
readme_md.append("")
readme_md.append("### Official JSON-LD Structured Data Schema")
readme_md.append("Below is the verified schema markup implemented on our web platform to power rich snippets and Google Knowledge Graph recognition:")
readme_md.append("")
readme_md.append("```json")
readme_md.append("""{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.shriramitventures.com/#organization",
      "name": "Shriram IT Ventures",
      "legalName": "Shriram IT Ventures",
      "url": "https://www.shriramitventures.com",
      "logo": "https://www.shriramitventures.com/images/logo.svg",
      "image": "https://www.shriramitventures.com/images/og-default.png",
      "description": "Shriram IT Ventures is a product engineering company based in Greater Noida (Delhi NCR). Since 2019 we’ve helped startups and enterprises design, build, and scale custom software, AI features, SaaS platforms, and mobile apps with weekly demos, honest estimates, and overlapping delivery hours for the US, UK, UAE, Canada, Australia, and India.",
      "email": "info@shriramitventures.com",
      "telephone": "+919548481594",
      "foundingDate": "2019",
      "sameAs": [
        "https://www.linkedin.com/company/shriram-it-ventures",
        "https://github.com/shriramitventures",
        "https://clutch.co/profile/shriram-it-ventures",
        "https://www.goodfirms.co/company/shriram-it-ventures",
        "https://www.g2.com/products/shriram-it-ventures/reviews",
        "https://twitter.com/shriramit",
        "https://www.facebook.com/shriramitventures",
        "https://www.youtube.com/@shriramitventures"
      ],
      "areaServed": ["India", "United States", "United Kingdom", "United Arab Emirates", "Canada", "Australia"]
    },
    {
      "@type": ["LocalBusiness", "ProfessionalService"],
      "@id": "https://www.shriramitventures.com/#localbusiness-greaternoida",
      "name": "Shriram IT Ventures — Greater Noida Studio",
      "url": "https://www.shriramitventures.com",
      "telephone": "+919548481594",
      "email": "info@shriramitventures.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Ajnara Homes",
        "addressLocality": "Greater Noida",
        "addressRegion": "Uttar Pradesh",
        "postalCode": "201304",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "28.5355",
        "longitude": "77.3910"
      },
      "openingHours": "Mo-Fr 09:30-18:30"
    }
  ]
}""")
readme_md.append("```")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# FAQ
readme_md.append("## ❓ Frequently Asked Questions (FAQ)")
readme_md.append("")
readme_md.append("### What does Shriram IT Ventures actually build?")
readme_md.append("We build custom web and multi-tenant SaaS products, production-grade AI/LLM/RAG features, native and cross-platform mobile apps (iOS & Android), resilient cloud/DevOps infrastructure, cybersecurity hardening, custom ecommerce engines, and code-level technical SEO systems.")
readme_md.append("")
readme_md.append("### Do you work with international clients across different time zones?")
readme_md.append("Yes. Over 60% of our client base is located in the **United States, United Kingdom, United Arab Emirates (Dubai), Canada, and Australia**. Our delivery squads maintain daily overlapping operational hours, conduct async updates via Loom/Slack, and follow English-first communication standards.")
readme_md.append("")
readme_md.append("### How long does a typical software project take from start to launch?")
readme_md.append("A typical Discovery Sprint takes **1 to 2 weeks**. Fixed-scope MVP builds typically land in **8 to 16 weeks**. Larger enterprise platforms ship in phased 2-week iterations with working software demoed every Friday.")
readme_md.append("")
readme_md.append("### What engagement models do you offer?")
readme_md.append("We offer three primary engagement models: **Discovery Sprints** for planning and de-risking, **Fixed-Scope Builds** for well-defined MVPs, and **Dedicated Product Squads** (monthly retainers) for ongoing product development and scaling.")
readme_md.append("")
readme_md.append("### Can you refactor or optimize an existing application without a full rewrite?")
readme_md.append("Yes. We frequently conduct technical code, security, and Core Web Vitals audits on existing codebases. We implement the Strangler Fig pattern or targeted refactoring sprints to modernize legacy systems, upgrade framework versions, and boost SEO rankings without risky full-system shutdowns.")
readme_md.append("")
readme_md.append("### How do you handle intellectual property (IP) and source code ownership?")
readme_md.append("You retain **100% complete ownership** of all source code, git repositories, architectural documentation, and cloud infrastructure from day one. We operate strictly under standard non-disclosure agreements (NDAs) and full IP assignment agreements.")
readme_md.append("")
readme_md.append("---")
readme_md.append("")

# Contact & Office Locations
readme_md.append("## 📞 Contact Channels & Global Office Locations")
readme_md.append("")
readme_md.append("Ready to turn a messy technical brief into a shippable plan? Contact our engineering team for an initial scoping conversation and honest estimate within 1 business day:")
readme_md.append("")
readme_md.append("### 📍 Greater Noida Headquarters (Delhi NCR)")
readme_md.append("- **Address**: Ajnara Homes, Greater Noida, Uttar Pradesh 201304, India")
readme_md.append("- **Google Maps Location**: [View on Google Maps](https://share.google/uHG8F632J36RhvVme)")
readme_md.append("- **Telephone**: [+91 95484 81594](tel:+919548481594)")
readme_md.append("- **Direct Email**: [info@shriramitventures.com](mailto:info@shriramitventures.com)")
readme_md.append("")
readme_md.append("### 📍 Aligarh Engineering Studio")
readme_md.append("- **Address**: Rambag Colony Gali No 6, Ramghat Road, Aligarh, Uttar Pradesh 202001, India")
readme_md.append("- **Google Maps Location**: [View on Google Maps](https://share.google/RKnOldGmgG5TZ4uz3)")
readme_md.append("")
readme_md.append("### 🌐 Online Consultation & Project Booking")
readme_md.append("- 📅 **Schedule a Discovery Call**: [https://www.shriramitventures.com/schedule-a-call](https://www.shriramitventures.com/schedule-a-call)")
readme_md.append("- 📝 **Request a Detailed Scope Quote**: [https://www.shriramitventures.com/get-quote](https://www.shriramitventures.com/get-quote)")
readme_md.append("- 🤖 **Consult AI Solution Architect**: [https://www.shriramitventures.com/solution-architect](https://www.shriramitventures.com/solution-architect)")
readme_md.append("- 🏢 **Explore All Capabilities**: [https://www.shriramitventures.com/services](https://www.shriramitventures.com/services)")
readme_md.append("")
readme_md.append("### 🔗 Connect With Us Online")
readme_md.append("- **GitHub**: [github.com/shriramitventures](https://github.com/shriramitventures)")
readme_md.append("- **LinkedIn**: [linkedin.com/company/shriram-it-ventures](https://www.linkedin.com/company/shriram-it-ventures)")
readme_md.append("- **Twitter / X**: [@shriramit](https://twitter.com/shriramit)")
readme_md.append("- **YouTube**: [@shriramitventures](https://www.youtube.com/@shriramitventures)")
readme_md.append("- **Facebook**: [facebook.com/shriramitventures](https://www.facebook.com/shriramitventures)")
readme_md.append("- **Instagram**: [@shriramitventures](https://www.instagram.com/shriramitventures)")
readme_md.append("")
readme_md.append("---")
readme_md.append("")
readme_md.append("<p align=\"center\">")
readme_md.append("  <b>Shriram IT Ventures</b> — Engineered for founders and operators who ship, not slides.<br>")
readme_md.append("  © 2019–2026 Shriram IT Ventures. All Rights Reserved.")
readme_md.append("</p>")

full_content = "\n".join(readme_md) + "\n"

with open("/Users/praveenrajpoot/Downloads/Projects/shriramgit/README.md", "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated README.md with {len(readme_md)} lines ({len(full_content)} characters)!")
