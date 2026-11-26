import Link from "next/link";
import { getTask } from "../../_lib/server";

export default async function TaskDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const task = await getTask((await params).id);

  return (
    <>
      <h1>ToDo Detail!!!</h1>
      <Link href="/">タスク一覧へ戻る</Link>
      <table>
        <tbody>
          <tr>
            <th>Item:</th>
            <td>{task.title}</td>
          </tr>
          <tr>
            <th>Desc:</th>
            <td>{task.description}</td>
          </tr>
        </tbody>
      </table>
    </>
  );
}
