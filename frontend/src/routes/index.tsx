import { createFileRoute } from "@tanstack/react-router"

export const Route = createFileRoute("/")({
  component: HomePage,
})

function HomePage() {
  return (
    <main style={{ padding: 24 }}>
      <h1>DRB+ Home</h1>
      <p>React + TanStack Router + Django API</p>
    </main>
  )
}
