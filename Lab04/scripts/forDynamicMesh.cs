using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public class forDynamicMesh : MonoBehaviour
{

    private Vector3[] vertices;
    private Vector2[] uv;
    private int[] triangles;
    private Mesh mesh;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Test");
        vertices = new Vector3[4 *40 *40];
        uv = new Vector2[4 *40 *40];
        triangles = new int[6 *40 *40];
        mesh = new Mesh();
        float delta = (float)(1.0 / 40);
        for (int i = 0; i < 40; i++)
        {
            for (int j = 0; j < 40; j++)
            {
                int index = i *40 + j;
                vertices[index * 4 + 0] = new Vector3((float)((1.0 / 8.0) * i - 2.5), (float)((1.0 / 8.0) * j - 2.5), 0);
                vertices[index * 4 + 1] = new Vector3((float)((1.0 / 8.0) * i - 2.5), (float)((1.0 / 8.0) * (j + 1) - 2.5), 0);
                vertices[index * 4 + 2] = new Vector3((float)((1.0 / 8.0) * (i + 1) - 2.5), (float)((1.0 / 8.0) * (j + 1) - 2.5), 0);
                vertices[index * 4 + 3] = new Vector3((float)((1.0 / 8.0) * (i + 1) - 2.5), (float)((1.0 / 8.0) * j - 2.5), 0);

                uv[index * 4 + 0] = new Vector2(i * delta, j * delta);
                uv[index * 4 + 1] = new Vector2(i * delta, (j + 1) * delta);
                uv[index * 4 + 2] = new Vector2((i + 1) * delta, (j + 1) * delta);
                uv[index * 4 + 3] = new Vector2((i + 1) * delta, j * delta);

                triangles[index * 6 + 0] = index * 4 + 0;
                triangles[index * 6 + 1] = index * 4 + 1;
                triangles[index * 6 + 2] = index * 4 + 2;
                triangles[index * 6 + 3] = index * 4 + 0;
                triangles[index * 6 + 4] = index * 4 + 2;
                triangles[index * 6 + 5] = index * 4 + 3;


            }
        }
        mesh.Clear();
        mesh.vertices = vertices;
        mesh.uv = uv;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
        GetComponent<MeshFilter>().mesh = mesh;

    }


    // Update is called once per frame
    void Update()
    {
        int a = 2;
        float v_height;
        float t = Time.time;
        for (int i = 0; i < vertices.Length; i++)
        {
            v_height = (float)(Mathf.Cos(Mathf.PI * vertices[i].x) * Mathf.Cos(Mathf.PI * vertices[i].y) * Mathf.Sin(a * t));
            vertices[i].z = v_height;
        }
        mesh.vertices = vertices;
        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
        GetComponent<MeshFilter>().mesh = mesh;
    }
}