import Form from "next/form";
import Link from "next/link";
import LogoutButton from "./_components/LogoutButton";
import { getMe, getTasks } from "./_lib/server";

export default async function TaskListPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const value = (await searchParams)["search-text"];
  const searchText = typeof value === "string" ? value : "";
  const [me, tasks] = await Promise.all([getMe(), getTasks(searchText)]);

  return (
    <>
      <div className="header">
        <h1>{me.username} のタスク</h1>
      </div>

      <div className="searchWrapper">
        <Form action="/">
          <input
            key={searchText}
            className="searchInput"
            type="text"
            name="search-text"
            defaultValue={searchText}
          />
          <input className="searchButton" type="submit" value="Search!!!" />
        </Form>

        <Link href="/tasks/new/" className="addTaskButton">
          タスク作成
        </Link>
      </div>

      <div className="taskListWrapper">
        {tasks.length === 0 && <div>No task data!</div>}
        {tasks.map((task) => {
          const title = <Link href={`/tasks/${task.id}/`}>{task.title}</Link>;
          return (
            <div className="taskWrapper" key={task.id}>
              <div className="taskTitle">
                <div className="taskCompleted">{task.completed ? "✅" : "☑️"}</div>
                {task.completed ? <s>{title}</s> : title}
              </div>
              <div className="taskEdit">
                <Link href={`/tasks/${task.id}/edit/`} className="updateButton">
                  ✏️ Edit
                </Link>{" "}
                <Link href={`/tasks/${task.id}/delete/`} className="deleteButton">
                  ❌ Delete
                </Link>
              </div>
            </div>
          );
        })}
      </div>

      <div className="loginAndLogout">
        <LogoutButton />
      </div>
    </>
  );
}
