// Server Component から Django の API を呼ぶ関数
import { cookies } from "next/headers";
import { notFound, redirect } from "next/navigation";
import type { Task, User } from "./types";

const djangoUrl = process.env.DJANGO_URL ?? "http://127.0.0.1:8000";

async function get<T>(path: string): Promise<T> {
  // サーバー側の fetch には Cookie が自動で付かないので、ブラウザの Cookie を渡す
  const response = await fetch(`${djangoUrl}${path}`, {
    headers: { Cookie: (await cookies()).toString() },
    cache: "no-store",
  });
  if (response.status === 403) redirect("/login/");
  if (response.status === 404) notFound();
  if (!response.ok) throw new Error(`API error: ${response.status}`);
  return response.json();
}

export function getMe() {
  return get<User>("/api/auth/me/");
}

export function getTasks(searchText: string) {
  const query = new URLSearchParams({ "search-text": searchText });
  return get<Task[]>(`/api/tasks/?${query}`);
}

export function getTask(id: string) {
  // URL の値をそのまま API のパスに使わない
  if (!/^\d+$/.test(id)) notFound();
  return get<Task>(`/api/tasks/${id}/`);
}
