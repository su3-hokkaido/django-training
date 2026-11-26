// ブラウザから Django の API を呼ぶ関数 (作成、更新、削除、ログインなど)

type Result = { ok: true } | { ok: false; errors: string[] };

function readCookie(name: string) {
  const row = document.cookie.split("; ").find((c) => c.startsWith(`${name}=`));
  return row?.slice(name.length + 1);
}

// Django は {項目名: [メッセージ]} か {detail: メッセージ} の形でエラーを返す
function toMessages(data: Record<string, string | string[]>) {
  return Object.entries(data).flatMap(([field, value]) => {
    const prefix = ["detail", "__all__", "non_field_errors"].includes(field) ? "" : `${field}: `;
    return [value].flat().map((message) => `${prefix}${message}`);
  });
}

export async function apiFetch(
  path: string,
  method: "POST" | "PATCH" | "DELETE",
  body?: object,
): Promise<Result> {
  try {
    if (!readCookie("csrftoken")) await fetch("/api/auth/csrf/");
    const response = await fetch(path, {
      method,
      headers: {
        "Content-Type": "application/json",
        // ログインするとトークンが変わるので、毎回 Cookie から読む
        "X-CSRFToken": readCookie("csrftoken") ?? "",
      },
      body: body && JSON.stringify(body),
    });
    if (response.ok) return { ok: true };
    // タスクの操作で 403 ならセッション切れの可能性がある
    if (response.status === 403 && path.startsWith("/api/tasks/")) {
      // 画面の古いキャッシュを残さないように、ページ全体を読み込み直す
      // eslint-disable-next-line @next/next/no-location-assign-relative-destination
      window.location.assign("/login/");
    }
    return { ok: false, errors: toMessages(await response.json()) };
  } catch {
    return { ok: false, errors: ["通信に失敗しました。もう一度試してください。"] };
  }
}
